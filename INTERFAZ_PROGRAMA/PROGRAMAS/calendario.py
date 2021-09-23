#librerías calendar

from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

#chatbot librerías------------------------

import speech_recognition as sr
import pyttsx3, pywhatkit

from time import strftime
#servicio google---------------------------

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendario_id = 'c_diiv2vljporasfr88fmus4c54o@group.calendar.google.com'

#-------------------------------------------

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#---------------------------------------------



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


def run_mike():  #importar esta función para la interfaz gráfica

    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    numeros2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    meses = {"enero": 1, "febrero": 2, "marzo" : 3, "abril" : 4, "mayo" : 5, "junio" : 6, "julio" : 7, "agosto" : 8, "septiembre" : 9, "octubre" : 10, "noviembre" : 11, "diciembre" : 12}

    contador2 = 0
    contador = 0
    minutos = 0
    hora = ""
    mes = 0 
    dia = ""
    mensajito = ""
    titulou = ""

    talk("Para añadir el evento, primero me tienes que decir el día, después el mes y finalmente la hora")
    rec = listen()
    print(rec)

    for i in rec:
        if i == " ":
            contador += 1
        if i in numeros:
            if contador == 0:
                dia += i

    for i in meses:
        if i in rec:
            mes += meses[i]
    
    for i in rec[12:60]:
        if i == ":":
            contador2 += 1
        if i in numeros2:
            if contador2 == 0:
                hora += i
    
    if "tarde" in rec:
        hora = int(hora) + 12

    else:
        pass

    if "30" in rec:
        minutos += 30
    
    if "15" in rec:
        minutos += 15
    
    if "tres cuartos" in rec:
        minutos += 45

    print("Día: ", dia, "  Mes: ", mes, "    Hora: ", hora,  "  Minutos: ", minutos )


#preguntar por el título
    
    talk("¿Qué título quieres que le ponga al evento?")
    rec = listen()
    titulou = str(rec)
    print(titulou)



#CREARCION DE UN EVENTO 

    hour_adjustment = -2
    event_request_body = {
        'start': {
            "dateTime": convert_to_RFC_datetime(int(strftime("%Y")), int(mes), int(dia), int(hora) + hour_adjustment , int(minutos) ),
            "timeZone": "Europe/Zurich"
        },
        "end": {
            "dateTime": convert_to_RFC_datetime(int(strftime("%Y")), int(mes), int(dia), int(hora) + hour_adjustment, int(minutos) ),
            "timeZone": "Europe/Zurich"
        },
        "summary": titulou,
        "description": titulou,
        "colorId": 5,
        "status": "confirmed",
        "transparency": "opaque",
        "visibility": "private",
        "location": "Chicago, IL",
        "attachments": [
            {
                "fileUrl": "https://drive.google.com/file/d/1GnmQHK6EgcEwHHoOyFREGcgBrstYs_9J/view",
                "title": "Invitation Letter Template in Word Doc"
            }
        ],
        "attendees": [
            {
                "displayName": "JJ",
                "comment": "I enjoy coding",
                "email": "dpue303@ibellvitge.net",
                "optional": False,
                "organizer": True,
                "responseStatus": "accepted"
            }
    
        ],
    }

    maxAttendees = 5
    sendNotification = True
    sendUpdate = "none"
    supportsAttachments = True

    response = service.events().insert(
        calendarId = calendario_id,
        maxAttendees=maxAttendees,
        sendNotifications= sendNotification,
        sendUpdates = sendUpdate,
        supportsAttachments=supportsAttachments,
        body=event_request_body

    ).execute()
    talk("Evento añadido a Google Calendar")
    print(titulou)
    




