import speech_recognition as sr
from src.input import get_audio
from src.error_exception import SpeechRecognitionError

def recognize_audio(r, audio, languages=['en-US']):
    """
    Function to recognize speech from audio data using Google's speech recognition API.
    
    Parameters:
    - r: Speech recognizer instance
    - audio: Audio data
    - languages: List of language codes (default is English)
    
    Returns:
    - Transcribed text
    """
    try:
        for language in languages:
            try:
                transcribed_text = r.recognize_google(audio, language=language)
                return transcribed_text, language
            except sr.UnknownValueError:
                continue
        # If no transcription is successful
        raise SpeechRecognitionError("Unable to recognize speech in any of the specified languages")
    except sr.RequestError:
        raise SpeechRecognitionError("Could not request results; check your internet connection")
    except Exception as e:
        raise SpeechRecognitionError("Error occurred during speech recognition: {}".format(e))


def recognize_audio_wrapper(r, languages=['en-US']):
    """
    Function to capture audio input and recognize speech.
    
    Parameters:
    - r: Speech recognizer instance
    - languages: List of language codes (default is English)
    
    Returns:
    - Transcribed text
    """
    try:
        audio = get_audio(r)
        return recognize_audio(r, audio, languages)
    except Exception as e:
        raise SpeechRecognitionError("Error occurred during audio capture: {}".format(e))
