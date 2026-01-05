import re
from urllib.request import urlopen


def main(inputData):
    # Fetch the .IMP text from the Zapier-provided URL.
    s3_pointer = inputData["geometry"]

    with urlopen(s3_pointer) as response:
        data = response.read()

    text = data.decode("utf-8", errors="replace")

    points = []
    meta = {}

    # Parse CompeGPS .IMP headers and calibration points.
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("Datum="):
            meta["datum"] = line.split("=", 1)[1].strip()
            continue

        if line.startswith("Projection="):
            meta["projection"] = line.split("=", 1)[1].strip()
            continue

        if line.startswith("Bitmap="):
            meta["bitmap"] = line.split("=", 1)[1].strip()
            continue

        if line.startswith("BitmapWidth="):
            value = line.split("=", 1)[1].strip()
            try:
                meta["bitmap_width"] = int(value)
            except ValueError:
                meta["bitmap_width"] = value
            continue

        if line.startswith("BitmapHeight="):
            value = line.split("=", 1)[1].strip()
            try:
                meta["bitmap_height"] = int(value)
            except ValueError:
                meta["bitmap_height"] = value
            continue

        if not re.match(r"^P\d+=", line):
            continue

        _, rest = line.split("=", 1)
        parts = [part.strip() for part in rest.split(",")]
        if len(parts) < 5:
            continue

        try:
            lon = float(parts[-2])
            lat = float(parts[-1])
        except ValueError:
            continue

        points.append((lon, lat))

    if len(points) < 2:
        raise ValueError("Not enough calibration points in input data")

    # Build a bounding polygon from calibration points.
    lons = [point[0] for point in points]
    lats = [point[1] for point in points]
    min_lon, max_lon = min(lons), max(lons)
    min_lat, max_lat = min(lats), max(lats)

    polygon = [
        [min_lon, min_lat],
        [max_lon, min_lat],
        [max_lon, max_lat],
        [min_lon, max_lat],
        [min_lon, min_lat],
    ]

    feature = {
        "type": "Feature",
        "properties": {
            "source": meta.get("bitmap"),
            "datum": meta.get("datum"),
            "projection": meta.get("projection"),
            "bitmap_width": meta.get("bitmap_width"),
            "bitmap_height": meta.get("bitmap_height"),
            "calibration_points": [{"lon": lon, "lat": lat} for lon, lat in points],
        },
        "geometry": {"type": "Polygon", "coordinates": [polygon]},
    }

    output = {"type": "FeatureCollection", "features": [feature]}

    # Return the GeoJSON payload as the Zapier step output.
    return {"data": output}
