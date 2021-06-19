import speech_recognition as sr
import pyttsx3, pywhatkit
import webbrowser


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
            rec = rec.lower(0)            #if name in rec:
                #rec = rec.replace(name, "")

    except:
        pass
    return rec


def run_juanita():
    rec = listen()
    if "noticias" in rec:
        webbrowser.open('https://www.lavanguardia.com/')
    
    if "YouTube" in rec:
        webbrowser.open("https://www.youtube.com")
    
    if "Amazon" in rec:
        print("¿Quieres comprar algo en específico?")
        talk("¿Quieres comprar algo en específico?")
        rec = listen()
        if "" in rec:
            webbrowser.open("https://www.amazon.es/s?k="+rec+"&__mk_es_ES=ÅMÅŽÕÑ&ref=nb_sb_noss_2")
        else:
            webbrowser.open("https://www.amazon.es/")

    if "Wikipedia" in rec:
        print("¿Qué quieres buscar?")
        talk("¿Qué quieres buscar?")
        rec = listen()

        if "" in rec:
            webbrowser.open("https://en.wikipedia.org/wiki/"+rec)
        else:
            pass


if __name__ == "__main__":
    run_juanita()