import speech_recognition as sr
import pyttsx3, pywhatkit
from time import gmtime, strftime

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
            #if name in rec:
                #rec = rec.replace(name, "")

    except:
        pass
    return rec

def runn():

            #rec = listen()
            #if "bloc de notas" in rec:    
                talk("¿Título?")
                rec = listen()

                if "" in rec:
                    archi1 = open(rec, "w")
                    archi1.write(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"\n")
                    talk("¿Qué quieres poner?")
                    rec = listen()

                    if "" in rec:
                        archi1.write(rec+"\n")
                        while True:
                            talk("¿Algo más?")
                            rec = listen()

                            if "si" in rec:
                                talk("Escuchando...")
                                rec = listen()
                                if "" in rec:
                                    archi1.write(rec+"\n")

                            if "no" in rec:
                                archi1.close()
                                talk("Bloc cerrado")
                                break
                            
                        

                else:
                    print(rec)
                    pass


runn()
