from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    "summary" : "San Francisco Events"
}

response = service.calendars().insert(body = request_body).execute()
print(response)

