import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init() 
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)


    except:
        pass
    return rec

def run_mike():
    talk("¿Título de la grabación?")
    rec = listen()
    tit = rec
    talk("Te escucho")
    with sr.Microphone() as source:
        audio = listener.listen(source)

        with open(tit + ".wav", "wb") as f:
            f.write(audio.get_wav_data())

    talk("Grabación finalizada")


run_mike()

