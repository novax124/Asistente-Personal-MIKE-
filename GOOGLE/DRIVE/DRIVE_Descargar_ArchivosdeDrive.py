import os 
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

servei = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

id_arxius = ["id de l'arxiu"]
nom_arxius = ["nom de l'arxiu"]

for id_arxiu, nom_arxiu in zip(id_arxius, nom_arxius):
    request = servei.files().get_media(fileId=id_arxiu)

    fh = io.BytesIO()
    descarregar = MediaIoBaseDownload(fd = fh, request=request)
    acabat = False

    while not acabat:
        status, acabat = descarregar.next_chunk()
        print("Download progress {0}".format(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join("./Photos", nom_arxiu), "wb") as f:
        f.write(fh.read())
        f.close()
