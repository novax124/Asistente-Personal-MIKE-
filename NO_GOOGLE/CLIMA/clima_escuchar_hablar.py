import speech_recognition as sr
import pyttsx3, pywhatkit
import requests
from pprint import pprint

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





def corre():
    rec = listen()
    if "tiempo" in rec:
        talk("¿En qué ciudad quieres saber el clima?")
        rec = listen()
        if "" in rec:
            city = rec
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=----url-----".format(city) 
            
            
            res = requests.get(url)

            data = res.json()


            temp = data["main"]["temp"]
            vel_viento = data["wind"]["speed"]

            latitud = data["coord"]["lat"]
            longitud = data["coord"]["lon"]

            descripcion = data["weather"][0]["description"]

            print("Temprerature: ", temp)              
            print("Wind Speed: {} m/s".format(vel_viento))
            print("Latitude: {}".format(latitud))
            print("Longitude: {}".format(longitud))
            print("Description: {}".format(descripcion))

corre()