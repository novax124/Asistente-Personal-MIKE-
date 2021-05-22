from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg ="Eyyy esto es una prueba python(mandando mensaje desde python"
mimeMessage = MIMEMultipart()
mimeMessage["to"] = "correodementira@gmail.com"
mimeMessage["subject"] = "Otra pruebaaaaaaa"  #titulo
mimeMessage.attach(MIMEText(emailMsg, "plain"))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
print(message)