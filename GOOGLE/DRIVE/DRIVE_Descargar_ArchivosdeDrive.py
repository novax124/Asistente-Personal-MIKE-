import os 
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ["id del archivo"]
file_names = ["nombre del archivo"]

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd = fh, request=request)
    done = False

    while not done:
        status, done = downloader.next_chunk()
        print("Download progress {0}".format(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join("./Photos", file_name), "wb") as f:
        f.write(fh.read())
        f.close()
