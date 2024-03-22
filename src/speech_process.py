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
                result = r.recognize_google(audio, language=language, result_output_format='json')
                result_dict = json.loads(result)
                transcribed_text = result_dict['alternative'][0]['transcript']
                return transcribed_text, language
            except sr.UnknownValueError:
                continue
        # If no transcription is successful
        raise sr.UnknownValueError("Unable to recognize speech in any of the specified languages")
    except sr.RequestError:
        raise Exception("Could not request results; check your internet connection")

def recognize_audio_wrapper(r, languages=['en-US']):
    """
    Function to capture audio input and recognize speech.
    
    Parameters:
    - r: Speech recognizer instance
    - languages: List of language codes (default is English)
    
    Returns:
    - Transcribed text
    """
    audio = get_audio(r)
    return recognize_audio(r, audio, languages)
