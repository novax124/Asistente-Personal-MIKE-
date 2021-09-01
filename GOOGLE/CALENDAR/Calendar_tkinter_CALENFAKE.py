from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
from tkinter import *


CLIENT_SECRET_FILE = "trchatbot.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id_chicago = 'calendar ID'

root = Tk()
miframe = Frame(root, width= 650, height= 650)
miframe.pack()

poneranio = 2
ponermes = 2
ponerdia = 2
ponerhora = 2
ponerminutos = 2

poneranio2 = 2
ponermes2 = 2
ponerdia2 = 2
ponerhora2 = 2
ponerminutos2 = 2

ponertitulo = 2
ponermensaje = 2

#programa------------------------------------

def accion():
    global poneranio
    global ponermes
    global ponerdia
    global ponerhora
    global ponerminutos
    global poneranio2
    global ponerdia2
    global ponermes2
    global ponerhora2
    global ponerminutos2
    global ponertitulo
    global ponermensaje

    poneranio = aniou.get()
    ponermes = mesu.get()
    ponerdia = diasu.get()
    ponerhora = horasu.get()
    ponerminutos = minutous.get()

    poneranio2 = aniou2.get()
    ponermes2 = mesu2.get()
    ponerdia2 = diasu2.get()
    ponerhora2 = horasu2.get()
    ponerminutos2 = minutous2.get()

    ponertitulo = titulou.get()
    ponermensaje = mensajito.get("1.0", END)

    poner()


def poner():

    hora = -2
    events = {
        'start': {
            
            "dateTime": convert_to_RFC_datetime(int(poneranio), int(ponermes), int(ponerdia), int(ponerhora) + hora , int(ponerminutos)),    #importante
            "timeZone": "Europe/Zurich"
        },
        "end": {
            "dateTime": convert_to_RFC_datetime(int(poneranio2), int(ponermes2), int(ponerdia2), int(ponerhora2) + hora , int(ponerminutos2)),         #importante
            "timeZone": "Europe/Zurich"
        },
        "summary": ponertitulo,                                                       
        "description": ponermensaje,                                    
        "colorId": 5,
        "status": "confirmed",
        "transparency": "opaque",
        "visibility": "private",
        "location": "Chicago, IL",
        "attachments": [
            {
                "fileUrl": "url document drive",
                "title": "títol document"
            }
        ],
        "attendees": [
            {
                "comment": "comentari",
                "email": "correu electrònic",
                "responseStatus": "accepted"
            }
    
        ],


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
        body= events

    ).execute()

    pprint(response)

    eventId = response["id"]


#-----label--------------------

calendariofake = Label(miframe, text = "CALENFAKE", fg = "yellow", font = ("Comic Sans MS", 40))
calendariofake.place(x = 150, y = 10)

empieza = Label(miframe, text = "Empieza:")      
empieza.place(x = 20, y = 110)
anio = Label(miframe, text = "Año:" )           
anio.place(x = 100, y = 110)
mes = Label(miframe, text= "Mes:")              
mes.place(x = 200, y = 110)
dia = Label(miframe, text= "Dia:")              
dia.place(x = 300, y = 110)
hora = Label(miframe, text= "Hora:")           
hora.place(x = 400, y = 110)
minutos = Label(miframe, text= "Minutos:")  
minutos.place(x = 500, y = 110)


acaba = Label(miframe, text = "Acaba:")      
acaba.place(x = 20, y = 210)
anio2 = Label(miframe, text = "Año:" )            
anio2.place(x = 100, y = 210)
mes2 = Label(miframe, text= "Mes:")               
mes2.place(x = 200, y = 210)
dia2 = Label(miframe, text= "Dia:")               
dia2.place(x = 300, y = 210)
hora2 = Label(miframe, text= "Hora:")            
hora2.place(x = 400, y = 210)
minutos2 = Label(miframe, text= "Minutos:") 
minutos2.place(x = 500, y = 210)


titulo = Label(miframe, text = "Título:")
titulo.place(x= 20, y = 310)

mensaje = Label(miframe, text = "Mensaje:")
mensaje.place(x= 20, y = 410)

#-------entrys--------------------------

aniou = StringVar()
cuadro1 = Entry(miframe, textvariable= aniou)
cuadro1.place(x= 130, y = 110, width= 50)
mesu = StringVar()
cuadro2 = Entry(miframe, textvariable= mesu)
cuadro2.place(x= 230, y = 110, width= 50)
diasu = StringVar()
cuadro3 = Entry(miframe, textvariable= diasu)
cuadro3.place(x= 330, y = 110, width= 50)
horasu = StringVar()
cuadro4 = Entry(miframe, textvariable= horasu)
cuadro4.place(x= 435, y = 110, width= 50)
minutous = StringVar()
cuadro5 = Entry(miframe, textvariable = minutous)
cuadro5.place(x= 555, y = 110, width= 50)


aniou2 = StringVar()
cuadro11 = Entry(miframe, textvariable=aniou2)
cuadro11.place(x= 130, y = 210, width= 50)
mesu2 = StringVar()
cuadro22 = Entry(miframe, textvariable= mesu2)
cuadro22.place(x= 230, y = 210, width= 50)
diasu2 = StringVar()
cuadro33 = Entry(miframe, textvariable = diasu2)
cuadro33.place(x= 330, y = 210, width= 50)
horasu2 = StringVar()
cuadro44 = Entry(miframe, textvariable= horasu2)
cuadro44.place(x= 435, y = 210, width= 50)
minutous2 = StringVar()
cuadro55 = Entry(miframe, textvariable= minutous2)
cuadro55.place(x= 555, y = 210, width= 50)

titulou = StringVar()
titulito = Entry(miframe, textvariable= titulou)
titulito.place(x =100, y =310, width = 250 )

mensajito = Text(miframe, width = 30, height = 10)     
mensajito.place(x = 100, y = 410)

scrollVert = Scrollbar(miframe, command= mensajito.yview) 
scrollVert.place(x=400, y = 455 )   

mensajito.config(yscrollcommand= scrollVert.set)


#------botón enviar-----------------------------------------------

enviar = Button(miframe, text = "ENVIAR", command = lambda:accion())
enviar.place(x = 200, y = 600)



root.mainloop()