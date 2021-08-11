import speech_recognition as sr
import pyttsx3, pywhatkit
import requests


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





def run_mike():
        talk("¿En qué ciudad quieres saber el clima?")
        rec = listen()
        if "" in rec:
            city = rec
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=   URL OBTENIDA   &units=metric".format(city) #.format importante
            
            
            res = requests.get(url)

            data = res.json()


            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]

            latitude = data["coord"]["lat"]
            longitude = data["coord"]["lon"]

            description = data["weather"][0]["description"]

            talk("La temperatura es: " + str(float(temp)))               
            talk("La velocidad del viento es:" + str(wind_speed))
            talk("La latitud es: " + str(latitude))
            talk("La longitud es: " + str(longitude))
            talk(description)

run_mike()