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

    buffer = []

    for row in tqdm(read_csv(args.input)):
        # -- Fill Buffer -- #
        link = row["BGG Link"]

        if not link:
            print("No BGG Link found.")
            continue
        else:
            game_id = extract_game_id(link)
            buffer.append(game_id)

        # -- Continue if buffer not full -- #
        if len(buffer) < 10:
            continue

        # -- Fetch Data -- #
        for game in fetch(buffer).findall(".//boardgame"):
            data = extract(game)
            # data["BGG Link"] = link
            print(data)

        # -- Clear Buffer -- #
        buffer = []
        break


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

    return parser.parse_args()


def read_csv(csvfile: str) -> list[dict[str, str]]:
    """Read a CSV file and return its content as a list of dictionaries."""
    with open(csvfile, "r") as input_file:
        reader = csv.DictReader(input_file)
        return list(reader)


def fetch(game_ids: list[str]) -> ET.Element:
    """Retrieve game information from BoardGameGeek."""

    response = httpx.get(
        "https://boardgamegeek.com/xmlapi/boardgame/" + ",".join(game_ids),
        follow_redirects=True,
    )

    data = ET.fromstring(response.content)
    return data


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


def extract(game: ET.Element) -> dict[str, str]:
    data = {}

    data["name"] = game.find(".//name[@primary='true']").text
    data["year"] = game.find(".//yearpublished").text

    data["players"] = {
        "min": game.find(".//minplayers").text,
        "max": game.find(".//maxplayers").text,
        "best": best_player_count(game),
    }

    data["playing_time"] = {
        "min": game.find(".//minplaytime").text,
        "max": game.find(".//maxplaytime").text,
        "avg": game.find(".//playingtime").text,
    }

    return data


################################
## if __name__ == "__main__": ##
################################

if __name__ == "__main__":
    main()
