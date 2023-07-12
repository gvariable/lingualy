from elevenlabs import generate, play
import time


voices = ["Sam", "Rachel", "Josh", "Elli", "Domi", "Bella", "Arnold", "Antoni", "Adam"]
for voice in voices:
    audio = generate(
        text="It is not in the stars to hold our destiny but in ourselves.", voice=voice
    )
    play(audio)
    time.sleep(0.5)
