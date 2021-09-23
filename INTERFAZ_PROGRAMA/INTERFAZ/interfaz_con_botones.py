######imports########

import collections
from SPOTIVOZ import escucharcancion
from MIKEELGRANDEGMAIL import run_mike2
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import webbrowser
from time import sleep


#####   EJECUCIÓN DE LOS PROGRAMAS    #####


def botones(rec):  #esta función se encarga de importar las funciones de cada programa que hemos hecho.

#from "programa" import "función"  <-- la función que se importará es aquella que hace la acción importante del programa.
#después, ejecutamos la función que se ha importado.

            #calendar código---------------------------------

                if rec == 2:                        
                    
                    from calendario import run_mike
                    run_mike()

            #gmail código---------------------

                if rec == 1:
                    from MIKEELGRANDEGMAIL import run_mike2
                    run_mike2()


            #código wikipedia

                if rec == 14:
                    from wikislamejor import escuchar
                    escuchar()


            #código youtube

                if rec == 11:
                    from youtube import run_mike3
                    run_mike3()


            #código amazon 
             
                if rec == 13:                         
                    from pruebascarritoamazonVOZ import run_mike4
                    run_mike4()


            #código spotify
                if rec == 4:
                    from SPOTIVOZ import escucharcancion
                    escucharcancion()


            #código bloc de notas

                if rec == 19:
                    from archivo1 import runn
                    runn()
            
            #código CLIMAVOZ

                if rec == 5:
                    from CLIMAVOZ import run_mike6
                    run_mike6()


            #código TRADUCTOR

                if rec == 3:
                    from TRADUCTORVOZ import empezar
                    empezar()


            #código diccionario

                if rec == 7:
                    from diccionario import pregunta
                    pregunta()

            #código noticias

                if rec == 12:
                    from leer_noticias_API_Buena2222 import run_mike7
                    run_mike7()
                
            #calculadora

                if rec == 9:
                    from calculadora import run_mike8
                    run_mike8()

            #grabadora

                if rec == 15:
                    from grabadoravoz import run_mike9
                    run_mike9()
                    
            #crono / cuenta atrás / alarma

                if rec == 8:
                    from crono import run_mike10
                    run_mike10()

                

            #buscador

                if rec == 6:
                    from buscadoor import run_mike11
                    run_mike11()

            
            #conversación

                if rec == 16:
                    from conversacion import run_mike12
                    run_mike12()


       


###### GIF ############## pondremos un gif en medio de la interfaz

class ImageLabel(tk.Label):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

print("holaa")
root = tk.Tk()
root.geometry("3000x3000")
root.config(background= "white", bg= "white")
lbl = ImageLabel(root, width=800, height=1100, background= "white")  #configuración tamaño del gif
lbl.pack()
lbl.load('asistente-robot5.gif')   #ponemos el gif que queramos dentro del paréntesis
miframe = Frame(root, width= 3000, height= 3000)
miframe.pack()

###### BOTONES CON LAS IMÁGENES #############

# en el parámetro "image" se pondrá la variable que se ha definido con una imagen, esta se pondrá encima de un botón para indicar al usuario que aplicación se estará utilizando al pulsarlo.

imagen2 = PhotoImage(file = "ygmail5.png")
b = Button(root, text = "Click", image = imagen2, background= "white", bg = "white", command= lambda:botones(1)).place(x = 10, y = 50)

imagen3 = PhotoImage(file = "ycalendar2.png")
c = Button(root, text = "Click", image = imagen3, background= "white", bg = "white", command= lambda:botones(2)).place(x = 10, y = 170)

imagen4 = PhotoImage(file = "ytrad2.png")
c = Button(root, text = "Click", image = imagen4, background= "white", bg = "white", command= lambda:botones(3)).place(x = 10, y = 290)

imagen5 = PhotoImage(file = "yspoti2.png")
c = Button(root, text = "Click", image = imagen5, background= "white", bg = "white", command= lambda:botones(4)).place(x = 10, y = 410)

imagen6 = PhotoImage(file = "ytiempo.png")
c = Button(root, text = "Click", image = imagen6, background= "white", bg = "white", command= lambda:botones(5)).place(x = 10, y = 530)

imagen7 = PhotoImage(file = "ybuscador.png")
c = Button(root, text = "Click", image = imagen7, background= "white", bg = "white", command= lambda:botones(6)).place(x = 10, y = 650)

imagen8 = PhotoImage(file = "ydiccionario.png")
c = Button(root, text = "Click", image = imagen8, background= "white", bg = "white", command= lambda:botones(7)).place(x = 10, y = 770)

imagen9 = PhotoImage(file = "yreloj.png")
c = Button(root, text = "Click", image = imagen9, background= "white", bg = "white", command= lambda:botones(8)).place(x = 10, y = 890)

imagen10 = PhotoImage(file = "ycalculadora2.png")
c = Button(root, text = "Click", image = imagen10, background= "white", bg = "white", command= lambda:botones(9)).place(x = 1770, y = 50)

imagen11 = PhotoImage(file = "yblocdenotas.png")
c = Button(root, text = "Click", image = imagen11, background= "white", bg = "white", command= lambda:botones(10)).place(x = 1770, y = 170)

imagen12 = PhotoImage(file = "yyoutube.png")
c = Button(root, text = "Click", image = imagen12, background= "white", bg = "white", command= lambda:botones(11)).place(x = 1770, y = 290)

imagen13 = PhotoImage(file = "ynoticias.png")
c = Button(root, text = "Click", image = imagen13, background= "white", bg = "white", command= lambda:botones(12)).place(x = 1770, y = 410)

imagen14 = PhotoImage(file = "yamazon.png")
c = Button(root, text = "Click", image = imagen14, background= "white", bg = "white", command= lambda:botones(13)).place(x = 1770, y = 530)

imagen15 = PhotoImage(file = "ywiki.png")
c = Button(root, text = "Click", image = imagen15, background= "white", bg = "white", command= lambda:botones(14)).place(x = 1770, y = 650)

imagen16 = PhotoImage(file = "ygrabadora.png")
c = Button(root, text = "Click", image = imagen16, background= "white", bg = "white", command= lambda:botones(15)).place(x = 1770, y = 770)

imagen17 = PhotoImage(file = "yconv.png")
c = Button(root, text = "Click", image = imagen17, background= "white", bg = "white", command= lambda:botones(16)).place(x = 1770, y = 890)



root.mainloop()