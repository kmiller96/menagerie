from tempfile import TemporaryDirectory
from pathlib import Path

from s2t import converter, transcriber
import typer

cli = typer.Typer()


@cli.command()
def main(audio_file: Path, output_file: Path):
    """Transcribes raw M4A audio to plain text."""
    with TemporaryDirectory() as tmpdir:
        tmpdir: Path = Path(tmpdir)

        converter.m4a_to_wav(audio_file, tmpdir / "audio.wav")
        transcription = transcriber.transcribe(tmpdir / "audio.wav")

        output_file.write_text(transcription)
