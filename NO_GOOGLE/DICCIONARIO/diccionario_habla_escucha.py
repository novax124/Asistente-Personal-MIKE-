from PyDictionary import PyDictionary
from googletrans import Translator
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
            rec = listener.recognize_google(pc, language = "es-Es")
            rec = rec.lower(0)

    except:
        pass
    return rec



dictionary=PyDictionary()

translator = Translator()

contador = 0
contador2 = 0
contador3 = 0



def pregunta():
    global contador 
    global contador2
    global contador3
    talk("Qué quieres preguntar?")
    rec = listen()
    resultado = str(translator.translate(rec, src = "es", dest = "en"))
    for i in resultado:
        contador += 1
        if i == ",":
            contador2 += 1
            if contador2 == 3:
                saber = contador
                contador2 = 0
                traduccion = resultado[33:saber -1]
            
        else:
            pass


    a = dictionary.meaning(str(traduccion))
    resultado2 = str(translator.translate(a, src = "en", dest = "es"))
    #print(resultado2)

    for i in resultado2:
        contador3 += 1
        if i == "]":
            traduccion2 = resultado2[33:contador3]
            break
            
        else:
            pass
        
    print(traduccion2)
    talk(traduccion2)





pregunta()
