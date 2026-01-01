import json
import re
from pathlib import Path

import typer


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    if not data_dir.exists():
        raise FileNotFoundError(f"Missing data directory: {data_dir}")

    imp_files = sorted(data_dir.glob("*.IMP"))
    if not imp_files:
        raise FileNotFoundError(f"No .IMP files found in {data_dir}")

    imp_path = imp_files[0]
    points = []
    meta = {}

    with imp_path.open("r", encoding="utf-8", errors="replace") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue

            if line.startswith("Datum="):
                meta["datum"] = line.split("=", 1)[1].strip()
                continue

            if line.startswith("Projection="):
                meta["projection"] = line.split("=", 1)[1].strip()
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
        raise ValueError(f"Not enough calibration points in {imp_path}")

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
            "source": imp_path.name,
            "datum": meta.get("datum"),
            "projection": meta.get("projection"),
            "bitmap_width": meta.get("bitmap_width"),
            "bitmap_height": meta.get("bitmap_height"),
            "calibration_points": [{"lon": lon, "lat": lat} for lon, lat in points],
        },
        "geometry": {"type": "Polygon", "coordinates": [polygon]},
    }

    geojson = {"type": "FeatureCollection", "features": [feature]}
    output_path = data_dir / f"{imp_path.stem}.geojson"
    output_path.write_text(json.dumps(geojson, indent=2), encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    typer.run(main)
