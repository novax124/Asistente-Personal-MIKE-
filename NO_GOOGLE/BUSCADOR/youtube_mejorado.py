import speech_recognition as sr
import pyttsx3, pywhatkit

import webbrowser
import pyautogui    

from time import sleep

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
    talk("¿Qué quieres hacer?")
    rec = listen()
    if "YouTube" in rec:
        webbrowser.open("https://www.youtube.com")

        talk("¿Quieres buscar algo en cocreto?")
        rec = listen()
        if "no quiero" in rec:
            pass
        else:
            webbrowser.open("https://www.youtube.com/results?search_query=" + str(rec))
            sleep(3)   
            pyautogui.press("tab")
            pyautogui.press("enter")

run_mike()

