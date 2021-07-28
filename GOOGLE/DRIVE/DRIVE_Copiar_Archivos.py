from Google import Create_Service


CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

servei = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

id_arxiu = "id del archivo"         
id_carpeta = ["id de la carpeta"]           

metadata = {
    "name" : "nom del arxiu",
    "parents" : id_carpeta,
    "description" : "descripció de l'arxiu"

}

servei.files().copy(
    fileId= id_arxiu,
    body= metadata
).execute()
