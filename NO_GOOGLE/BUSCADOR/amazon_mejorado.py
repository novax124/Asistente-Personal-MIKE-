import speech_recognition as sr
import pyttsx3, pywhatkit

import webbrowser
import pyautogui                

rango = 58
numero = 0
bajar = -1100

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
    global numero
    global rango
    global bajar

    talk("¿Qué quieres buscar?")
    rec = listen()

    if "Amazon" in rec:
        talk("¿Qué quieres comprar o mirar?")
        rec = listen()

        if "" in rec:
            webbrowser.open("https://www.amazon.es/s?k="+rec+"&__mk_es_ES=ÅMÅŽÕÑ&ref=nb_sb_noss")
            talk("¿Quieres comprar algo o mirar más modelos?")
            rec = listen()

            while True:
                if "comprar algo" in rec:
                    talk("¿Qué modelo quieres comprar?")
                    rec = listen()
            

                    if "uno" in rec:
                        pyautogui.click(1490,0)
                        numero += 6
                        for i in range(rango + numero):
                            pyautogui.press("tab")
                        pyautogui.typewrite(["enter"])
                        break
                
                    if "dos" in rec:
                        pyautogui.click(1490,0)
                        numero += 12
                        for i in range(rango + numero):
                            pyautogui.press("tab")
                        pyautogui.typewrite(["enter"])
                        break
               
                    if "tres" in rec:
                        pyautogui.click(1490,0)
                        numero += 18
                        for i in range(rango + numero):
                            pyautogui.press("tab")
                        pyautogui.typewrite(["enter"])
                        break
                
                    if "cuatro" in rec:
                        pyautogui.click(1490,0)
                        numero += 24
                        for i in range(rango + numero):
                            pyautogui.press("tab")
                        pyautogui.typewrite(["enter"])
                        break

                numero += 24

                if "mirar más modelos" in rec:
                        pyautogui.click(1908, 146)   #(1908, 146)
                        pyautogui.scroll(bajar)
                        bajar += -1100
                        talk("¿Quieres comprar algo o seguir mirando?")
                        rec = listen()

    talk("Hecho")
                    






run_mike()