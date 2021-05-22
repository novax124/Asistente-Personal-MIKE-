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
#pprint(colors)


recurrence = [    #cambiar datos
    "RRULE:FREQ=MONTHLY;COUNT=2" 
]

hour_adjustment = -8
event_request_body = {
    'start': {
        "dateTime": convert_to_RFC_datetime(2021, 5, 21, 12 + hour_adjustment ,45 ),
        "timeZone": "Asia/Taipei"
    },
    "end": {
        "dateTime": convert_to_RFC_datetime(2021,5,21,14 + hour_adjustment , 45 ),
        "timeZone": "Asia/Taipei"
    },
    "summary": "Family Lunch",
    "description": "Having lunch with the parents",
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
    "recurrence": recurrence  #datos nuevos

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

"""
Update Data
"""
"""
start_datetime = convert_to_RFC_datetime(2021, 5, 20, 12 + hour_adjustment ,45 )
end_datetime =  convert_to_RFC_datetime(2021,5,20,14 + hour_adjustment , 45 )
response["start"]["datetime"] = start_datetime
response["start"]["datetime"] = end_datetime
response["summary"] = "Family Dinner"
response["Description"] = "Having Family Dinner"
service.events().update(
    calendarId = calendar_id_chicago,
    eventId = eventId,
    body = response).execute()

"""