
#chatbot librerías------------------------

import speech_recognition as sr
import pyttsx3

#otras librerias-----------------------------

from time import sleep
import webbrowser
import pyautogui



#escuchar y hablar-------------------------------------
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#-----------------------------------------------

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
    while True:
        try:

            rec = listen()


            #clave activación MIKE ("ok Google")----------------------------

            if "hola asistente" in rec:
                print(rec)
                talk("te escucho")
                rec = listen()

            #poner lluvia--------------------------------------------

                if "lluvia" in rec:
                    webbrowser.open("https://www.youtube.com/watch?v=Z_fEKap24wU")  
                    sleep(5)
                    pyautogui.press("enter")
                    pyautogui.press("enter")


            #calendar código---------------------------------

                if "cita" in rec:                        
                    print(rec)
                    import calendario  


            #gmail código---------------------

                if "correo" in rec:
                    import gmail 


            #código wikipedia

                if "Wikipedia" in rec:
                    import wikipediaa


            #código youtube

                if "YouTube" in rec:
                    import youtube
                    print("algo")

                    
            #código amazon 
             
                if "Amazon" in rec:                      
                    import amazon


            #código spotify
                if "escuchar música" in rec:
                    import spotify

                if "escuchar canción" in rec:
                    import spotify

            #código bloc de notas

                if "bloc de notas" in rec:
                    import blocdenotas 
            
            #código CLIMAVOZ

                if "clima" in rec:
                    import clima 

                if "tiempo" in rec:
                    import clima

            #código TRADUCTOR

                if "traducir" in rec:
                    import traductor

                if "traductor" in rec:
                    import traductor

            #código diccionario

                if "diccionario" in rec:
                    import diccionario

            #código noticias

                if "noticias" in rec:
                    import noticias
                
            #calculadora

                if "calculadora" in rec:
                    import calculadora

            #grabadora

                if "grabadora" in rec:
                    import grabadoravoz
                    
            #crono / cuenta atrás / alarma

                if "reloj" in rec:
                    import crono 


            else:
                print(rec)
                talk("No te he entendido")

        except:
            talk("No te he entendido")




run_mike()
