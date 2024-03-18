def save_audio(audio, filename):
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())

def print_transcription(transcription):
    print("Look at what you said ...\n" + transcription)
    print("I also recorded your voice\n")