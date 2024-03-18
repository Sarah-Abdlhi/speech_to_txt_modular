import speech_recognition as sr
from input import get_audio
from output import save_audio, print_transcription
from speech_process import recognize_audio
from error_exception import SpeechRecognitionError, handle_error

def main():
    # Initialize speech recognizer
    r = sr.Recognizer()

    try:
        # Capture audio input
        audio = get_audio(r)
        # Recognize speech
        transcription = recognize_audio(r, audio)
        # Print transcription
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
