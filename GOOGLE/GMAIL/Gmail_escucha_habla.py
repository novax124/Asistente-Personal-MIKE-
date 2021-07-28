#gmail librerías --------------------------
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#chatbot librerías------------------------

import speech_recognition as sr
import pyttsx3, pywhatkit

#servidor google---------------------------------

CLIENT_SECRET_FILE = "cliente ID"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#------------------------------------

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#---------------------------------------------

mimeMessage = MIMEMultipart()

titulito = ""
mensajito = ""

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
    rec = listen()
    if "correo" in rec:
        print("¿A quién quieres que se lo envíe? ")
        talk("¿A quién quieres que se lo mande?")
        enviara()
    else:
        talk("No te he entendido")



def enviara():
    rec = listen()
    if "nombre de la persona" in rec:
        print("¿Título?")
        talk("¿Título?")
        tituloo()

def tituloo():
    rec = listen()
    if " " in rec:
        global titulito
        titulito = rec  
        print("¿Qué mensaje quieres que le envíe?")
        talk("¿Qué mensaje quieres que le envíe?")
        mensajee()

def mensajee():
    rec = listen()
    if " " in rec:
        global mensajito
        mensajito = rec
        print("¿Seguro que quieres que envíe este mensaje a David?")
        talk("¿Seguro que quieres que envíe este mensaje a David?")
        print(rec)
        seguroo()

def seguroo():
    rec = listen()
    if "Si" in rec:
        mimeMessage["to"] = "correomentira@gmail.com"
        mimeMessage["subject"] = titulito
        emailMsg = mensajito 
        mimeMessage.attach(MIMEText(emailMsg, "plain"))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
        print("Se ha enviado correctamente")
        talk("Se ha enviado correctamente")
    else:
        pass

                     


if __name__ == "__main__":
    run_mike()
