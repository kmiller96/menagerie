import typer


from hearts.main import play

cli = typer.Typer()


@cli.command()
def run():
    play([1, 2, 3, 4])
