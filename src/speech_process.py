import speech_recognition as sr

def recognize_audio(r, audio):
    """
    Function to recognize speech from audio data using Google's speech recognition API.
    
    Parameters:
    - r: Speech recognizer instance
    - audio: Audio data
    
    Returns:
    - Transcribed text
    """
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        raise Exception("Unable to recognize speech")
    except sr.RequestError:
        raise Exception("Could not request results; check your internet connection")
