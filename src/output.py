def save_audio(audio):
    """
    Function to save audio data to a WAV file.
    
    Parameters:
    - audio: Audio data to be saved
    """
    with open("ur_voice.wav", "wb") as f:
        f.write(audio.get_wav_data())

def print_transcription(transcription):
    """
    Function to print the transcription of speech.
    
    Parameters:
    - transcription: Transcribed text
    """
    print("Look at what you said ...\n" + transcription)
    print("I also recorded your voice\n")
