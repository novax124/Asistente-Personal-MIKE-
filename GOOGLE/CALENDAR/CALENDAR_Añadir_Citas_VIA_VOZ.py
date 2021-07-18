
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

#chatbot librerías------------------------

import speech_recognition as sr
import pyttsx3, pywhatkit



#servidor google---------------------------

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id_chicago = 'c_c6pdkmik4p1ff1qj1l86uc7j68@group.calendar.google.com'

#-------------------------------------------

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#---------------------------------------------
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

num = ""

meses = {"enero": 1, "febrero": 2, "marzo" : 3, "abril" : 4, "mayo" : 5, "junio" : 6, "julio" : 7, "agosto" : 8, "septiembre" : 9, "octubre" : 10, "noviembre" : 11, "diciembre" : 12}
dias = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9}
horas = {"una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9} 

anio1 = ""
anio2 = 0

ponermes = 0 
ponermes2 = 0

dia1 = 0
dia2 = 0

horas1 = ""
horas2 = 0

minutos1 = 0
minutos2 = 0

contador = 0

mensajito = ""
titul = ""


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

#---bien---------

def run_mike():
    talk("Te escucho")
    rec = listen()
    if "cita" in rec:
        print("¿Cuándo empieza la cita? ")
        talk("¿Cuándo empieza la cita? ")
        anio()
        

def anio():
    global anio1
    global numeros
    rec = listen()
    if "" in rec: 
        for i in rec:
            if i in numeros:
                anio1 += i
            else:
                pass
        
    print("¿Mes? ")
    talk("Mes? ")
    mes()
    
    

def mes():
    global ponermes
    global meses
    global contador
    rec = listen()
    if "" in rec:
        for i in meses:
            if rec in i:
                ponermes = meses[i]
                print(ponermes)                          
                print("¿Dia?")
                talk("¿Dia?")
                contador += 1
                
        
        if contador <= 0:
            if rec not in i:
                contador += 1
                talk("Di solamente el mes")
                print(rec)
                mes()

        diass()
        


def diass():
    global dia1
    global dias
    global contador
    rec = listen()
    if "" in rec:
        for i in dias:
            if rec in i:
                dia1 = dias[i]
                print(dia1)                          
                print("¿Hora?")
                talk("¿Hora?")
                horass()           
                break
               
        if rec not in i:
            dia1 = int(rec)
            print("¿Hora?")
            talk("¿Hora?")
            print(dia1)
            horass()
            

    

def horass():         
    global horas1
    global numeros
    global contador
    global horas
    rec = listen()
    print(rec)
    if "mañana" in rec:
        for i in horas:
            if rec in i:
                horas1 = horas[i]
                print("HA PASADO POR MAÑANA")
                print("¿Minuto?")
                talk("¿Minuto?")
                minutos()
                break
        if rec not in i:  
            for i in rec:  
                if i in numeros:
                    horas1 += i
                    print("HA PASADO POR MAÑANA2")
                    print("¿Minuto?")
                    talk("¿Minuto?")
                minutos()
                break

    if "tarde" in rec:    
        for i in horas:
            if rec in i:
                horas1 = 12 + horas[i]
                print("HA PASADO POR TARDE")
                print("¿Minuto?")
                talk("¿Minuto?")
                minutos()
                break
        if rec not in i:
            for i in rec:
                if i in numeros:
                    print(rec)          
                    print(i)
                    horas1 += str(12 + int(i))
                    print(horas1)
                    print("¿Minuto?")
                    talk("¿Minuto?")
                    minutos() 
                    break
                 
        
        


def minutos():
    global minutos1
    rec = listen()
    if "" in rec:                     
        minutos1 = int(rec)
        print("¿Cuando acaba?")
        talk("¿Cuando acaba?")
    alcabo()

def alcabo():
    global anio1
    global anio2
    global ponermes
    global ponermes2
    global dia1
    global dia2
    global horas1
    global horas2
    global minutos1
    global minutos2
    global numeros
    global num

    rec =listen()


    if "una hora" in rec:
        anio2 = anio1
        ponermes2 = ponermes
        dia2 = dia1
        horas2 = int(horas1) + 1
        minutos2 = minutos1
        

    if "un día" in rec:
        anio2 = anio1
        ponermes2 = ponermes
        dia2 = dia1 + 1
        horas2 = horas1
        minutos2 = minutos1
    

    if "media hora" in rec:
        anio2 = anio1
        ponermes2 = ponermes
        dia2 = dia1
        horas2 = horas1
        minutos2 = minutos1 + 30
    
    print("¿Título?")
    talk("¿Título?")
    
    titulo()

def titulo():
    global titul
    rec = listen()
    if "" in rec:
        titul = str(rec)
        print("¿Qué mensaje quieres que le ponga?")
        talk("¿Qué mensaje quieres que le ponga?")
        mensaje()

def mensaje():
    global mensajito
    rec = listen()
    if "" in rec:
        mensajito = str(rec)
        print("Cita añadida en tu calendario")
        talk("Cita añadida en tu calendario")
        print(anio1, anio2, ponermes, ponermes2, dia1, dia2, horas1, horas2, minutos1, minutos2)
    calendario()




def calendario():
    global anio1
    global anio2
    global ponermes
    global ponermes2
    global dia1
    global dia2
    global horas1
    global horas2
    global minutos1
    global minutos2
    global mensajito
    global titul
    colors = service.colors().get().execute()
    #pprint(colors)

    recurrence = [    #cambiar datos
        "RRULE:FREQ=WEEKLY;COUNT=5;BYDAY=TU,FR" 
    ]

    hour_adjustment = -2
    event_request_body = {
        'start': {
            "dateTime": convert_to_RFC_datetime(int(anio1), int(ponermes), int(dia1), int(horas1) + hour_adjustment , int(minutos1) ),
            "timeZone": "Europe/Zurich"
        },
        "end": {
            "dateTime": convert_to_RFC_datetime(int(anio2), int(ponermes2), int(dia2), int(horas2) + hour_adjustment, int(minutos2) ),
            "timeZone": "Europe/Zurich"
        },
        "summary": titul,
        "description": mensajito,
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
        calendarId = calendar_id_chicago,
        maxAttendees=maxAttendees,
        sendNotifications= sendNotification,
        sendUpdates = sendUpdate,
        supportsAttachments=supportsAttachments,
        body=event_request_body

    ).execute()

    pprint(response)
    
run_mike()