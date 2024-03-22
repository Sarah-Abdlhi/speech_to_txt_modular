import speech_recognition as sr

def recognize_audio(r, audio, languages=['en-US']):
    """
    Function to recognize speech from audio data using Google's speech recognition API.
    
    Parameters:
    - r: Speech recognizer instance
    - audio: Audio data
    
    Returns:
    - Transcribed text
    """
    try:
        for language in languages:
            try:
                return r.recognize_google(audio, language = language)
            except sr.UnknownValueError:
                continue
        # if no transcription is successful
        raise sr.UnknownValueError("Unable to recognize speech")
    except sr.RequestError:
        raise Exception("Could not request results; check your internet connection")
