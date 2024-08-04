import typer


from hearts.game import Game
from hearts.players import HumanPlayer, AIPlayer

cli = typer.Typer()


@cli.command()
def run():
    name = input("Enter your name: ")

    players = [
        HumanPlayer(name),
        AIPlayer("AI 1"),
        AIPlayer("AI 2"),
        AIPlayer("AI 3"),
    ]

    game = Game(players)
    game.play_game()
