import speech_recognition as sr
from src.input import get_audio
from src.output import save_audio, print_transcription
from src.speech_process import recognize_audio
from src.error_exception import SpeechRecognitionError

def main():
    r = sr.Recognizer()

    try:
        audio = get_audio(r)
        transcription = recognize_audio(r, audio)
        print_transcription(transcription)
        save_audio(audio, "ur_voice.wav")
    except SpeechRecognitionError as e:
        print("Speech recognition error:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()