import typer

cli = typer.Typer()


@cli.command()
def run():
    typer.echo("Hello!")
