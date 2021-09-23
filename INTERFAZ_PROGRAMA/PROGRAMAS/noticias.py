from newsapi import NewsApiClient
import newsapi

import datetime

import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

tday = datetime.date.today()
z = 4
h = 4
contador = 0
rec2 = ""

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



my_api_key = "llave api"  #poner llave de la api
newsapi = NewsApiClient(api_key=my_api_key)

def run_mike7(): #importar esta función para la interfaz gráfica
    global z
    global h
    global contador
    global rec2
    global tday
    talk("¿Quieres escuchar noticias generales o concretas?")
    rec = listen()

    if "noticias" in rec:
        data = newsapi.get_everything(q = "noticias", language= "es", page_size=5, from_param=tday)  
        articles = data["articles"]
        for x, y in enumerate(articles):        
            print(f'{x} {y["title"]}')
            talk(f'{x} {y["title"]}')

        while True:
            talk("¿Quieres saber más noticias o quieres escuchar una de estas?")
            rec = listen()

            if "primera" in rec:
                articles = data["articles"][contador]["content"]
                talk(articles)
                break
            
            if "segunda" in rec:
                contador += 1
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "tercera" in rec:
                contador += 2
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "cuarta" in rec:
                contador += 3
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "quinta" in rec:
                contador += 4
                articles = data["articles"][contador]["content"]
                talk(articles)
                break        
                
            if "más" in rec:  #saber más noticias
                data = newsapi.get_everything(q = "noticias", language= "es", page_size=20, from_param= tday) 
                articles = data["articles"][5]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][6]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][7]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][8]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][9]["title"]
                print(articles) 
                talk(articles)    
                contador += 5

    
    else:
        rec2 = rec
        data = newsapi.get_everything(q = rec2, language= "es", page_size=5, from_param=tday)  
        articles = data["articles"]
        for x, y in enumerate(articles):           
            print(f'{x} {y["title"]}')
            talk(f'{x} {y["title"]}')

        while True:
            talk("¿Quieres saber más noticias o quieres escuchar una de estas?")
            rec = listen()

            if "primera" in rec:
                articles = data["articles"][contador]["content"]
                talk(articles)
                break
            
            if "segunda" in rec:
                contador += 1
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "tercera" in rec:
                contador += 2
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "cuarta" in rec:
                contador += 3
                articles = data["articles"][contador]["content"]
                talk(articles)
                break

            if "quinta" in rec:
                contador += 4
                articles = data["articles"][contador]["content"]
                talk(articles)
                break        
                
            if "saber más noticias" in rec:
                data = newsapi.get_everything(q = rec2, language= "es", page_size=20, from_param= tday) 
                articles = data["articles"][5]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][6]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][7]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][8]["title"]
                print(articles) 
                talk(articles)  
                articles = data["articles"][9]["title"]
                print(articles) 
                talk(articles)    
                contador += 5


