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


    except:
        pass
    return rec





def run_mike6():   #importar esta función para la interfaz gráfica
        talk("¿En qué ciudad quieres saber el clima?")
        rec = listen()
        if "" in rec:
            city = rec
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=    poner id    &units=metric".format(city) 
            
            
            res = requests.get(url)

            data = res.json()


            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]

            latitude = data["coord"]["lat"]
            longitude = data["coord"]["lon"]

            description = data["weather"][0]["description"]

            talk("La temperatura es: " + str(temp))             
            talk("La velocidad del viento es:" + str(wind_speed))
            talk("La latitud es: " + str(latitude))
            talk("La longitud es: " + str(longitude))
            talk(description)

            print(rec)
            print("Temprerature: ", temp)                            #temperatura
            print("Wind Speed: ", wind_speed, "m/s")        #viento 
            print("Latitude: ", latitude)                   #latitud
            print("Longitude: ", longitude)                #longitud
            print("Description: ", description)             #decripción del ambiente


run_mike6()