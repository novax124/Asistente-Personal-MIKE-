import speech_recognition as sr
import pyttsx3
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
            rec = rec.lower(0)


    except:
        pass
    return rec

def run_mike11():
    talk("¿Qué quieres buscar?")
    rec = listen()
    webbrowser.open("https://www.google.es/search?q="+rec+"&safe=active&source=hp&ei=cR-qYPq9LoWPjLsPydmNqA8&iflsig=AINFCbYAAAAAYKotge5kB71oc-xT2NMeHrrOAanqyL-I&oq=españa&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMQCMgUIABDEAjIECAAQAzIECAAQAzIECAAQAzIECAAQAzICCCYyBAgAEB4yBAgAEB4yBAgAEB46BAgAEBM6BggAEAoQE1CcGljUOWCFPmgEcAB4AIABdYgB8gaSAQM2LjOYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=gws-wiz&ved=0ahUKEwi6urbyvd_wAhWFB2MBHclsA_UQ4dUDCAY&uact=5")

run_mike11()