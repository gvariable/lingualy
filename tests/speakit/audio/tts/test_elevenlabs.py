from speakit import ElevenLabsTTS


def test_elevenlabs_tts():
    tts = ElevenLabsTTS()
    audio = tts.generate("hello! How are you?")
    assert isinstance(audio, bytes)
    assert len(audio) > 0
