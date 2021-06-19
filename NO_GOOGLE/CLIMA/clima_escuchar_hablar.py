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
            #if name in rec:
                #rec = rec.replace(name, "")

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
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=----url-----".format(city) #.format importante
            
            
            res = requests.get(url)

            data = res.json()


            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]

            latitude = data["coord"]["lat"]
            longitude = data["coord"]["lon"]

            description = data["weather"][0]["description"]

            print("Temprerature: ", temp)                 #mismo problema que el de calendar / no puedo pasar de numeros a letras
            print("Wind Speed: {} m/s".format(wind_speed))
            print("Latitude: {}".format(latitude))
            print("Longitude: {}".format(longitude))
            print("Description: {}".format(description))

corre()