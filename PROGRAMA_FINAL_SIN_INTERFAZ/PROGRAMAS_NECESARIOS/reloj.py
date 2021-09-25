import webbrowser
import pyautogui
from time import sleep

import speech_recognition as sr
import pyttsx3

tiempo = {"cero" : 0, "una" : 1, "dos": 2, "tres" : 3, "cuatro" : 4, "cinco" : 5, "seis" : 6, "siete" : 7, "ocho" : 8, "nueve" : 9, "diez" : 10, "once" : 11}
tiempo2 = {"cero" : 0, "uno" : 1, "dos": 2, "tres" : 3, "cuatro" : 4, "cinco" : 5, "seis" : 6, "siete" : 7, "ocho" : 8, "nueve" : 9, "diez" : 10, "once" : 11}
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

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


def minutos():  #importar esta función para la interfaz gráfica
        talk("¿Minutos?")
        minutos = listen()
        for i in tiempo2:
            if minutos == i:
                pyautogui.press("tab")
                for i in range(tiempo2[i]):
                    pyautogui.press("down")
                pyautogui.press("enter")
        
        try:
            pyautogui.press("tab")
            for i in range(int(minutos)):
                pyautogui.press("down")
            pyautogui.press("enter")

        except:
            pass
        

def run_mike10():
    
    talk("¡Qué quieres hacer?")
    rec = listen()


    if "cronómetro" in rec:
        webbrowser.open("https://reloj-alarma.es/cronometro/#start=") 

    
    if "temporizador" in rec:
        webbrowser.open("https://reloj-alarma.es/temporizador/#countdown=00:00:00&enabled=0&seconds=0&sound=xylophone&loop=1")
        sleep(5)
        for i in range(11):
            pyautogui.press("tab")
        pyautogui.press("enter")
        sleep(2)
        for i in range(2):
            pyautogui.press("tab")

        talk("¿Horas?")
        horas = listen()
        print(horas)
        for i in tiempo:
            if horas == i:
                for i in range(tiempo[i]):
                    pyautogui.press("down")
                minutos()
        try:
                for i in range(int(horas)):
                    pyautogui.press("down")
                minutos()

        except:
            pass

    
    if "alarma" in rec:
        webbrowser.open("https://reloj-alarma.es/#time=00:00&title=Alarma&enabled=0&sound=guitar&loop=1")
        sleep(5)
        for i in range(11):
            pyautogui.press("tab")
        pyautogui.press("enter")
        sleep(2)                                            
        for i in range(2):
            pyautogui.press("tab")

        talk("¿Hora?")
        horas2 = listen()
        if "mañana" in horas2:
            for i in tiempo:
                if horas2 == i:
                    for i in range(tiempo[i]):
                        pyautogui.press("down")
                    minutos()
                    break
                
            else:
                print(horas2)
                for i in numeros:
                    for z in horas2:
                        if z == i:
                            for i in range(int(i)):
                                pyautogui.press("down")
                            minutos()

        if "tarde" in horas2:
            for i in tiempo:
                if horas2 == i:
                    print(tiempo[i])
                    for i in range(tiempo[i] + 12):
                        pyautogui.press("down")
                    minutos()
                    break

            else:
                print("holaaa")
                print(horas2)
                for i in numeros:
                    for z in horas2:
                        if z == i:
                            for i in range(int(i) + 12):
                                pyautogui.press("down")
                            minutos()
            

run_mike10()