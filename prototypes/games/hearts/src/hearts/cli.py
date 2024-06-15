import typer


from hearts.game import Game
from hearts.players import Player

cli = typer.Typer()


@cli.command()
def run():
    game = Game([Player(f"Player {i}") for i in range(4)])
    game.play_game()
