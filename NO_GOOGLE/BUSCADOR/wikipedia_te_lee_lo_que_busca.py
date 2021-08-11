import wikipedia
import speech_recognition as sr
import pyttsx3, pywhatkit


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



def escuchar():
    talk("Te escucho")
    rec = listen()
    pregunta = rec
    wikipedia.set_lang("es")
    res = wikipedia.summary(pregunta, sentences = 1)
    talk(res)


escuchar()

