def get_audio(r):
    with r.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("start talking and I will hopefully catch and transcribe it...")
        audio = r.listen(source)
        print("I am transcribing you ...\n")
    return audio