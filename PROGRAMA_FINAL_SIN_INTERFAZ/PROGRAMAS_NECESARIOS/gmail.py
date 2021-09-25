#gmail librerías ------------------------
from Google import Create_Service #teneis la libreria en la descripción
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#CHATBOT LIBRERÍAS

import speech_recognition as sr
import pyttsx3


# servidor de google 

CLIENTE = "trchatbot.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENTE, API_NAME, API_VERSION, SCOPES)

#--------------------------------------------

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#--------------------------


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language= "es-ES")
            rec = rec.lower(0)

    except:
        pass
    return rec 

def run_mike2():   #importar esta función para la interfaz gráfica
    print("¿A quién quieres que se lo envíe? ") 
    talk("¿A quién?")
    rec = listen()
    if "persona" in rec:  #poner nombre de la persona la cual quieres enviar el correo electrónico
        print("Título?")
        talk("Título?")
        tituloo()

def tituloo():
    rec = ""
    rec = listen()
    if " " in rec:
        global titulito
        titulito = ""
        titulito = rec
        print("¿Qué mensaje quieres que le envíe?")
        talk("¿Qué mensaje quieres que le envíe?")
        mensajee()


def mensajee():
    rec = ""
    rec = listen()
    if " " in rec:
        global mensajito
        mensajito = ""
        print(rec)
        print(mensajito)
        mensajito = rec
        print("¿Seguro que quieres enviar este mensaje?")
        talk("¿Seguro que quieres enviar este mensaje?")
        print(rec)
        print(mensajito)
        seguroo()

def seguroo():


    mimeMessage = MIMEMultipart()

    print(titulito)
    print(mensajito)
    rec = listen()
    if "claro" in rec:
        mimeMessage["to"] = "correo electrónico"   #poner correo electrónico de la persona
        mimeMessage["subject"] = titulito
        emailMsg = mensajito
        mimeMessage.attach(MIMEText(emailMsg, "plain"))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId = "me", body = {"raw":raw_string}).execute()
        print("Se ha enviado correctamente")
        talk("Se ha enviado correctamente")

    else:
        pass
    

run_mike2()



