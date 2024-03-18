import speech_recognition as sr

def recognize_audio(r, audio):
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        raise Exception("Unable to recognize speech")
    except sr.RequestError:
        raise Exception("Could not request results; check your internet connection")