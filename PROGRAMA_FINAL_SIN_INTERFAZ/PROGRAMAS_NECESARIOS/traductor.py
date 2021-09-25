from googletrans import Translator
#from googletrans.models import Translated
import speech_recognition as sr
import pyttsx3, pywhatkit


listener = sr.Recognizer()

#habla en castellano------------------

translator = Translator()



#habla en castellano ----------------

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    
    engine.say(text)
    engine.runAndWait()

#habla en inglés -------------------

def talk2(text):
    engine2 = pyttsx3.init()
    voices = engine2.getProperty("voices")
    engine2.setProperty("voice", voices[1].id)

    engine2.say(text)
    engine2.runAndWait()
#-------------------------------------------


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

def listen2():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower(0)
            #if name in rec:
                #rec = rec.replace(name, "")
    except:
        pass
    return rec



def empezar(): #importar esta función para la interfaz gráfica

    texto = ""
    resultado = ""
    contador = 0
    contador2 = 0
    saber = 0

    talk("¿Quieres traducir del inglés al castellano o del castellano al inglés?")
    print("¿Quieres traducir del inglés al castellano o del castellano al inglés?")
    rec = listen()
    if "del inglés al castellano" in rec:
        print("Qué quieres decir?")
        talk("Qué quieres decir?")
        rec = listen2()
        if "" in rec: 
            texto = rec
            resultado = str(translator.translate(texto, src = "en", dest = "es"))
            for i in resultado:
                contador +=1
                if i == ",":
                    contador2 +=1
                    if contador2 == 3:
                        saber = contador
                        contador2 = 0
                        talk(resultado[33:saber])
                        print(resultado)
                        break
                    else:
                        pass



    
    else:
        print("Qué quieres decir?")
        talk("Qué quieres decir?")
        rec = listen()
        if "" in rec: 
            texto = rec
        resultado = str(translator.translate(texto, src = "es", dest = "en"))  
        for i in resultado:
            contador +=1
            if i == "=":
                contador2 +=1
                if contador2 == 4:
                    saber = contador
                    contador2 = 0
                    talk2(resultado[33:saber - 18])
                    print(resultado)
                    break
                else:
                    pass   
       

empezar()
