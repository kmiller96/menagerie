import argparse
import csv
from xml.etree import ElementTree as ET

import httpx
from tqdm import tqdm


##################
## Main Routine ##
##################


def main():
    args = parse_cli()

    buffer: list[tuple[int, str]] = []
    output: list[dict] = []

    rows = read_csv(args.input)

    for n, row in enumerate(tqdm(rows)):
        # -- Fill Buffer -- #
        link = row["BGG Link"]

        if not link:
            continue

        buffer.append((n, link))

        # -- Continue if buffer not full -- #
        if len(buffer) > 10 or n == len(rows) - 1:
            row_ids = [x[0] for x in buffer]
            game_ids = [extract_game_id(x[1]) for x in buffer]

            # -- Fetch Data -- #
            for n, game in zip(row_ids, fetch(game_ids).findall(".//boardgame")):
                data = extract(game)

                data["row"] = n
                data["link"] = link

                output.append(data)

            # -- Clear Buffer -- #
            buffer = []

        else:
            continue

    # -- Format Output -- #
    write_csv(output, args.output)


#################
## Subroutines ##
#################


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Enrich input data using BoardGameGeek."
    )

    parser.add_argument(
        "input",
        type=str,
        help="Path to the input file containing the data to enrich.",
    )

    parser.add_argument(
        "output",
        type=str,
        help="Path to the output file where the enriched data will be saved.",
    )

    parser.add_argument(
        "--chunksize",
        type=int,
        default=10,
        help="Number of games to fetch in each request.",
    )

    return parser.parse_args()


def read_csv(csvfile: str) -> list[dict[str, str]]:
    """Read a CSV file and return its content as a list of dictionaries."""
    with open(csvfile, "r") as input_file:
        reader = csv.DictReader(input_file)
        return list(reader)


def write_csv(data: list[dict[str, str]], csvfile: str):
    """Write a list of dictionaries to a CSV file."""
    keys = data[0].keys()

    with open(csvfile, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


def fetch(game_ids: list[str]) -> ET.Element:
    """Retrieve game information from BoardGameGeek."""
    response = httpx.get(
        "https://boardgamegeek.com/xmlapi/boardgame/" + ",".join(game_ids),
        follow_redirects=True,
    )

    data = ET.fromstring(response.content)
    return data


def extract(game: ET.Element) -> dict[str, str]:
    data = {}

    data["name"] = game.find(".//name[@primary='true']").text
    data["year"] = game.find(".//yearpublished").text

    data["players_min"] = game.find(".//minplayers").text
    data["players_max"] = game.find(".//maxplayers").text
    data["players_best"] = best_player_count(game)

    data["playing_time_min"] = game.find(".//minplaytime").text
    data["playing_time_max"] = game.find(".//maxplaytime").text
    data["playing_time_avg"] = game.find(".//playingtime").text

    return data


#############
## Helpers ##
#############


def extract_game_id(link: str) -> str:
    """Extracts the game ID from a BoardGameGeek link."""
    return link.split("/")[-2]


def best_player_count(game: ET.Element) -> str:
    results = {}

    for option in game.findall(".//poll[@name='suggested_numplayers']/results"):
        numplayers = option.attrib["numplayers"]
        numvotes = option.find(".//result[@value='Best']").attrib["numvotes"]

        results[numplayers] = numvotes

    return max(results, key=results.get)


################################
## if __name__ == "__main__": ##
################################

if __name__ == "__main__":
    main()
