import elevenlabs
from elevenlabs import generate
from pydub import AudioSegment
import io
import os
import time
from io import BytesIO
import base64

elevenlabs.set_api_key("2e49450c1538492b9083bfd5786dc43e")

# Defining a function to generate Arabic speech audio from a text answer
def arabic_speech_answer(ar_answer):
    if ar_answer:
        audio = generate(
            text=ar_answer,
            voice="Daniel",
            model='eleven_multilingual_v2'
        )
    else:
        print("▶️ empty ar_answer")
    audio = AudioSegment.from_file(io.BytesIO(audio), format="mp3")
    audio.export("output.mp3", format="mp3")

    return audio.duration_seconds

def text_to_speech():
    with open("output.mp3", "rb") as audio_file:
      audio_data = audio_file.read()
    audio_base64 = base64.b64encode(audio_data).decode("utf-8")
    audio_player = f'<audio src="data:audio/mpeg;base64,{audio_base64}" controls autoplay></audio>'
    return audio_player