from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep

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




client_id = 'cliente_id'  #poner la id
client_secret = 'cliente_secreto'  #poner la id
flag = 0


author = ''
song = ''

def escucharcancion():   #importar esta función para la interfaz gráfica
    global song
    talk("¿Qué canción quieres escuchar?")
    rec = listen()
    if "" in rec:
        song = rec.upper()
        empezar()

    else: 
        pass

def empezar():
    global flag
    global song

    if len(author) > 0:

        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = sp.search(author)

        for i in range(0, len(result["tracks"]["items"])):
            name_song = result["tracks"]["items"][i]["name"].upper()

            if song in name_song:
                flag = 1
                web.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                break
                         
            
    if flag == 0:
        song = song.replace(" ", "%20")
        web.open(f'spotify:search:{song}')
        sleep(5)
        for i in range(27):                
            pyautogui.press("tab")
        pyautogui.press("enter")
        
      
     
