import speech_recognition as sr

def get_audio(r):
    """
    Function to capture audio input from the microphone.
    
    Parameters:
    - r: Speech recognizer instance
    
    Returns:
    - audio: Captured audio data via Mic
    """
    # with makes sure mic is properly released once block exited
    #opens microphone
    # a class provided by the speech_recognition library, representing microphone as the audio input source
    with sr.Microphone() as source:
        # Adjust microphone for ambient noise
        r.adjust_for_ambient_noise(source)
        print("start talking and I will hopefully catch and transcribe it...")
        # Capture audio
        audio = r.listen(source)
        print("I am transcribing you ...\n")
    return audio
