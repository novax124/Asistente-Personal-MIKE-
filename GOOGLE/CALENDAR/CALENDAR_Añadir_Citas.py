from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime


CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id_chicago = 'id del calendar'

"""
Create an event
"""
colors = service.colors().get().execute()
pprint(colors)  #no es necesario hacer este print


hour_adjustment = -2
event_request_body = {
    'start': {
        "dateTime": convert_to_RFC_datetime(2021, 5, 21, 12 + hour_adjustment ,45 ),
        "timeZone": "zona horaria"
    },
    "end": {
        "dateTime": convert_to_RFC_datetime(2021,5,21,14 + hour_adjustment , 45 ),
        "timeZone": "zona horaria"
    },
    "summary": "título del evento",
    "description": "descripción del evento",
    "colorId": 5,
    "status": "confirmed",
    "transparency": "opaque",
    "visibility": "private",
    "location": "localidad",
    "attachments": [
        {
            "fileUrl": "url de documento de drive",
            "title": "título del documento de drive"
        }
    ],
    "attendees": [
        {
            "displayName": "nombre",
            "comment": "comentario",
            "email": "correo electrónico",
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

eventId = response["id"]

