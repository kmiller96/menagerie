from pathlib import Path

import typer

cli = typer.Typer()


@cli.command()
def main(audio_file: Path, output_file: Path):
    typer.echo(f"Converting {audio_file} to text...")
    typer.echo(f"Saving text to {output_file}...")
