import typer

from hearts.deck import Deck

cli = typer.Typer()


@cli.command()
def run():
    deck = Deck()
    deck.shuffle()

    for card in deck:
        print(card)
