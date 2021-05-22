from Google import Create_Service


CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

source_file_id = "id del archivo"         
folder_ids = ["id de la carpeta"]           

file_metadata = {
    "name" : "nombre para el archivo",
    "parents" : folder_ids,
    "starred" : True,
    "description" : "descripción del archivo"

}

service.files().copy(
    fileId= source_file_id,
    body=file_metadata
).execute()
