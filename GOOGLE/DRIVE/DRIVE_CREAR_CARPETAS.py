from Google import Create_Service

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

carpetas = ["Nombre carpetaaaa"]

for carpeta in carpetas:
    file_metadata = {
        "name" : carpeta,
        "mimeType" : "application/vnd.google-apps.folder"
        #"parents" : []
    }

    service.files().create(body=file_metadata).execute()
