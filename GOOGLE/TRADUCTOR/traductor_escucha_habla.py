from googletrans.models import Translated
import speech_recognition as sr
import pyttsx3, pywhatkit
import googletrans
from googletrans import Translator

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)

translator = Translator()

texto = ""


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
            #if name in rec:
                #rec = rec.replace(name, "")

    except:
        pass
    return rec


def empezar():
    global texto
    rec = listen()
    if "traducir del español al inglés" in rec:
        talk("¿Qué quieres traducir?")
        rec = listen()
        if "" in rec:
            texto = rec
            print(translator.translate(texto, src = "es", dest = "en"))





empezar()