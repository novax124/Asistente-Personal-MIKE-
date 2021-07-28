from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

id_carpeta = "id de la carpeta"
nom_arxius = ["nom de l'arxiu"]
tipus = ["image/jpeg   <-- en cas de que sigui una imatge tipus jpg"]

for nom_arxiu, tip in zip(nom_arxius, tipus):
    metadata = {
        "name" : nom_arxiu,
        "parents" : [id_carpeta]
    }

    media = MediaFileUpload("./Drive/{0}".format(nom_arxiu), mimetype=tip)

    service.files().create(
        body= metadata,
        media_body = media,
        fields = "id"
    ).execute()

    