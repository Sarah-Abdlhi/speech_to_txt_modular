import speech_recognition as sr
from src.input import get_audio
from src.output import save_audio, print_transcription
from src.speech_process import recognize_audio
from src.error_exception import SpeechRecognitionError, handle_error

def main():
    # Initialize speech recognizer
    r = sr.Recognizer()  # Create an instance of the Recognizer class

    try:
        # Capture audio input
        audio = get_audio(r)
        # Recognize speech
        transcription, language = recognize_audio(r, audio, languages=['en-US', 'fa-IR', 'de-DE'])
        # Print transcription
        if language == 'fa-IR':  # If Persian language is detected
            # Display the transcribed text from right to left
            print("Look at what you said ...\n" + transcription[::-1])
        else:
            print_transcription(transcription)
        # Save audio data
        save_audio(audio)
    except SpeechRecognitionError as e:
        # Handle speech recognition errors
        handle_error(e)
    except Exception as e:
        # Handle other errors
        handle_error(e)

if __name__ == "__main__":
    main()
