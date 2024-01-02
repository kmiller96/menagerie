from pathlib import Path

from pydub import AudioSegment


def m4a_to_wav(input_path: Path, output_path: Path):
    """Converts M4A audio to WAV audio. This is needed for GCP (for some reason)."""
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio.export(output_path, format="wav")
