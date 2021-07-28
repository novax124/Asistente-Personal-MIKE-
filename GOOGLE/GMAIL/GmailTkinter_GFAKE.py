from tkinter import *
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "cliente ID"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


root = Tk()
miframe = Frame(root, width= 650, height= 650)
miframe.pack()

#-------gmail-----------------------------
mimeMessage = MIMEMultipart()

def enviarcorreo():
    if enviara.get() == "PERSONA 1":
        mimeMessage["to"] = "correomentira@gmail.com"
        accion()

    if enviara.get() == "PERSONA 2":
        mimeMessage["to"] = "correomentir2@gmail.com"
        accion()

    else:
        pass

    
def accion():
    emailMsg = textoComentario.get("1.0", END)
    mimeMessage["subject"] = tituloo.get() 

    mimeMessage.attach(MIMEText(emailMsg, "plain"))                          
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
    print(message)



#--------text-----------------

nombre_correo = Label(miframe, text = "GFAKE", fg = "red", font = ("Comic Sans MS", 40)).grid(row = 0, column = 1, padx = 10, pady = 10)
poner_correo = Label(miframe, text = "Enviar a...:").grid(row= 1, column = 0, padx = 10, pady = 10)
titulo = Label(miframe, text = "Título:").grid(row= 2, column = 0, padx = 10, pady = 10)
texto = Label(miframe, text = "Mensaje:").grid(row = 3, column= 0, padx = 10, pady=10)

#------cuadros--------------------

enviara = StringVar()
primercuadro = Entry(miframe, textvariable= enviara).grid(row = 1, column= 1)

tituloo = StringVar()
segundocuadro = Entry(miframe, textvariable= tituloo).grid(row = 2, column= 1)


textoComentario = Text(miframe, width = 30, height = 10)    # no se si está bien  
textoComentario.grid(row = 3, column = 1)

scrollVert = Scrollbar(miframe, command= textoComentario.yview) 
scrollVert.grid(row = 3, column = 2, sticky= "nsew")   

textoComentario.config(yscrollcommand= scrollVert.set)

#-------botón_enviar---------------------------

enviar = Button(miframe, text = "Enviar", command= enviarcorreo).grid(row = 4, column = 3)
#borrar = Button(miframe, text = "Borrar", command = borrartodo).grid(row = 4, column = 3)                        

root.mainloop()