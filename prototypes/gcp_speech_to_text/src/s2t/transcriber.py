from pathlib import Path

import speech_recognition as sr


def transcribe(input_file: Path) -> str:
    """Transcribes the WAV file using GCP."""
    ## Setup recognizer class
    recognizer = sr.Recognizer()

    ## Load the audio data.
    with sr.AudioFile(str(input_file.absolute())) as source:
        audio_data = recognizer.record(source)

    ## Submit it to GCP
    return recognizer.recognize_google_cloud(audio_data)
