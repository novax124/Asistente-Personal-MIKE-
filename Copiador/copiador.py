from tkinter import *
from time import sleep, gmtime, strftime
import speech_recognition as sr
import pyttsx3, pywhatkit


root = Tk()
root.title("Copiador")
root.geometry("800x800")
root.config(background= "steel blue")
miframe = Frame(root, background= "steel blue", width= 650, height= 650)
miframe.pack()



listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='ca-CA')
            rec = rec.lower(0)


    except:
        pass
    return rec


#----------programa---------------------------

def escuchando():
    rec = listen()
    #resultado = str(translator.translate(rec, src = "en", dest = "es"))
    textoComentario.insert(INSERT, rec)
    textoComentario.insert(INSERT, "\n")



def crear():
    cuadroprimero = enviara.get()
    archi1 = open(cuadroprimero, "w")
    archi1.write(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"\n")
    archi1.write(textoComentario.get("1.0", END))

#--------text-----------------

nombre_nombre_archivo = Label(miframe,background= "steel blue", text = "COPIADOR", fg = "SeaGreen2", font = ("Comic Sans MS", 40)).grid(row = 0, column = 1, pady = 10)
poner_nombrearchivo = Label(miframe, text = "Nombre del archivo").grid(row= 1, column = 1, padx = 10, pady = 10)
#titulo = Label(miframe, text = "Título:").grid(row= 2, column = 0, padx = 10, pady = 10)
#texto = Label(miframe, text = "Mensaje:").grid(row = 3, column= 0, padx = 10, pady=10)


#------cuadros--------------------

enviara = StringVar()
primercuadro = Entry(miframe, textvariable= enviara).grid(row = 2, column= 1)

#tituloo = StringVar()
#segundocuadro = Entry(miframe, textvariable= tituloo).grid(row = 2, column= 1)


textoComentario = Text(miframe, width = 65, height = 15)    # no se si está bien  
textoComentario.grid(row = 4, column = 1)

scrollVert = Scrollbar(miframe, command= textoComentario.yview) 
scrollVert.grid(row = 4, column = 2, sticky= "nsew")   

textoComentario.config(yscrollcommand= scrollVert.set)


#-------botón_enviar---------------------------

escuchar = Button(miframe, text = "Escuchar", width= 30, height = 5, background="DarkOliveGreen3", command= lambda:escuchando()).grid(row = 3, column = 1, pady = 35)
creararchivo = Button(miframe, text = "Crear archivo", command= lambda:crear()).grid(row = 5, column = 1, padx = 20, pady = 25)
#borrar = Button(miframe, text = "Borrar", command = borrartodo).grid(row = 4, column = 3)                        

root.mainloop()