from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime


CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendari = 'id del calendar'

"""
Crear un event
"""
colors = service.colors().get().execute()
pprint(colors)  


hora = -2
events = {
    'start': {
        "dateTime": convert_to_RFC_datetime(2021, 5, 21, 12 + hora ,45 ),
        "timeZone": "zona horaria"
    },
    "end": {
        "dateTime": convert_to_RFC_datetime(2021,5,21,14 + hora , 45 ),
        "timeZone": "zona horaria"
    },
    "summary": "título del evento",
    "description": "descripció del event",
    "colorId": 5,
    "status": "confirmed",
    "visibility": "private",
    "location": "localitat",
    "attachments": [
        {
            "fileUrl": "url de documento de drive",
            "title": "título del documento de drive"
        }
    ],
    "attendees": [
        {
            "comment": "comentario",
            "email": "correu electrónico",
            "responseStatus": "accepted"
        }
    
    ],
   

}

maxAttendees = 5
sendNotification = True
sendUpdate = "none"
supportsAttachments = True

response = service.events().insert(
    calendarId = calendari,
    maxAttendees=maxAttendees,
    sendNotifications= sendNotification,
    sendUpdates = sendUpdate,
    supportsAttachments=supportsAttachments,
    body=events

).execute()

pprint(response)

eventId = response["id"]

