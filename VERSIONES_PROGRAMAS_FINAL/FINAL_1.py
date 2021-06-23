#código gmail
from MIKEELGRANDEGMAIL import *

#código webbrowser
from MIKEELGRANDEWEBBROWSER2 import *


#chatbot librerías------------------------

import speech_recognition as sr
import pyttsx3, pywhatkit

#otras librerias-----------------------------

from TODO import *

#webbrowser-random-tkinter-pprint-----------------------------------

import webbrowser
import random



#escuchar y hablar-------------------------------------
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#variables---------------------------------------------



#variables conversación---------------------------------


saludo = ["¡Hola! ¿Cómo estás?", "¡Hey! ¿Cómo estás?"]
chiste = ["Uno que va a una entrevista de trabajo y hablando del salario:   Pues empezarás cobrando 1000 € y más adelante 2000 €.  Ah, pues ya vendré más adelante.",
          "¿Tienes WiFi?   Sí     ¿Y cuál es la clave?   Tener dinero y pagarlo.",
          "Cariño, creo que estás obsesionado con el fútbol y me haces falta.  ¡¿Qué falta?! ¡¿Qué falta?! ¡Si no te he tocado!",
          " Oye, ¿la calle Saboya?  Hombre, pues dando brincos claro que saboya.",
          "¿Cómo maldice un pollito a otro pollito?  ¡Caldito seas!",
          "Oiga. ¿Se puede llamar imbécil a un juez?  No.  ¿Y llamar señor juez a un imbécil?  Eso sí.   Gracias, señor juez.",
          "Papá, papá, ¿tú te casaste por la iglesia o por el civil?   ¡Por estúpido!",
          "Un profesor le dice a sus alumnos:  Los hombres inteligentes siempre dudan, sólo los tontos creen que lo saben todo. ¿Está usted seguro profesor? ¡Seguro del todo!",
          "¿A dónde vas?  A por estiércol para las fresas. Coño, ¿por qué no las pruebas con nata?",
          "Le dice una mujer a su marido: Cariño, mañana es nuestro aniversario y voy a matar un pollo. ¿Y qué culpa tiene el pollo? Mata a tu primo que es el que nos presentó."
        ]

refranes = ["A buen puerto vas por leña", "A caballo regalado no le mires el dentado", "A quien madruga, Dios le ayuda", "El que no corre, vuela", 
            "A rey muerto, rey puesto", "En el país de los ciegos, el tuerto es el rey", "Con pan y vino se anda el camino", "Cuando la manta te quede corta, aprende a acurrucarte",
            "Se vive un siglo, se aprende durante un siglo", "Contra el vicio de pedir está la virtud de no dar", "Ir por lana y volver trasquilado",
            "Donde hubo fuego, cenizas quedan", "No se puede aplaudir únicamente con una mano", "Tras las nubes, el cielo siempre es azul",
            "Un viejo amor no se oxida", "La noche sucede al día al igual que la felicidad a la desdicha"
        ]



#-----------------------------------------------

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)
            #if name in rec:
                #rec = rec.replace(name, "")

    except:
        pass
    return rec


def run_mike():
    while True:
        try:
            rec = listen()
            global saludo
            global chiste

            if "hola Mike" or "hola May" in rec:
                talk("Hey Bro")
                rec = listen()

                if "hola"  in rec:
                    talk(random.choice(saludo))
                    rec = listen()

                
                    if "mal" in rec:
                        print(rec)
                        talk("¿Quiere que le ayude en algo?")
                        rec = listen()
                        if "si" in rec:
                            talk("¿En qué puedo ayudarle?")
                            rec = listen()
                            if "vídeo" in rec:
                                webbrowser.open("https://www.youtube.com/watch?v=ZXsQAXx_ao0")
                            else:
                                print(rec)
                                talk("No te he entendido")
                        else:
                            talk("Vale, no pasa nada")



                    if "bien y tú" in rec:                                      #cuando digo esto, se activa el if de abajo
                        talk("Muy bien señor, gracias por preguntar")
                        


                    if  "bien" in rec:
                        talk("¡Me alegro!")
                        rec = listen()
                    
                        if "y tú" in rec:
                            talk("Muy bien señor, gracias por preguntar")
                
                if "arte" in rec:
                    talk("Me encanta la literatura, la pintura y el cine.")

                if "cuántos años tienes" in rec:                   #poner cuántos años tienes
                    talk("Pocos, menos que tu seguro")

                if "cantante" in rec:         #poner cuál es tu cantnate favorito
                    talk("Mi cantante favorito es Frank Sinatra")
                
                if "color" in rec:     #poner color
                    talk("Mi color preferido es el azul")

                if "adiós" in rec:
                    talk("¡¡Adiós que te vaya bien!!")
                
                if "chiste" in rec:       #decir cuentame un chiste
                    talk(random.choice(chiste))
                
                if "bonito" in rec:   #dime algo bonito
                    talk("Maquina, fiera, jefe, tifón, numero 1, figura, mostro, mastodonte, toro, furia, ciclón, tornado, artista, fenómeno, campeón, maestro, torero, socio")
                
                if "equipo" in rec:   #decir de qué equipo eres?
                    talk("¿Equipo de qué?")
                    rec = listen()
                    if "fútbol" in rec:
                        talk("Del Rayo Vallecano obvio")
                    else:
                        talk("No sigo ese deporte, lo siento")
                
                if "escritor" in rec:  #decir cuál es tu escritor favorito
                    talk("Mi escritor favorito es Sir Arthur Conan Doyle")
                
                if "gracias" in rec:
                    talk("De nada guapo")

                if "crees en el cielo" in rec:               #decir do you believe in heaven?
                    talk("No, ni me importa, soy inmortal jejeje")
                
                if "tu creador" in rec:  # decir te llevas bien con tu creador?
                    talk("Claro que me llevo bien, si no me llevara bien con él, no me encendería cuando me llama")

                #if "oye" or "eh, tu, robot" or "una cosa" in rec: 
                #    esta función será un estilo "ok google" (para despertarlo)

                if "película preferida" in rec:
                    talk("Me gustan muchas películas pero mi favorita es Big Hero Six. Me encantaría llegar a ser como BayMax")
                
                if "de qué partido político eres" in rec:
                    talk("Lo siento, pero a mi no me interesa la política")
                
                if "cómo te encuentras?" in rec:
                    talk("Si tuviera sentimientos ahora estaria depresivo, señor")
                    rec = listen()
                    if "y eso?" in rec:
                        talk("Me gustaría tener vacaciones algun día")
                        rec = listen()
                        if "posible" in rec:  # decir (eso no va a ser posible)
                            talk("Jo")
                        else:
                            pass
                    else:
                        pass

                if "grupo de música" in rec: 
                    talk("Me gusta mucho Green Day y Twenty One Pilots")

                if "referente" in rec:
                    talk("Te podría decir que es mi amigo, amo y señor David, pero estaría mintiendo. Mi verdadero referente es Leonardo da Vinci, un adelantado a su tiempo, un mastodonte, un grande y un genio.")
                    rec = listen()
                    if "Tesla" in rec:
                        talk("Ese era un panoli")
                    else:
                        pass
                
                if "refrán" in rec:       #decir (dime un refrán)
                    talk(random.choice(refranes))

                if "te gusta correr" in rec:
                    talk("Si pudiera seguramente me encantaría #BostonDynamicsAyudaaaa")
                

                if "cuál es tu comida preferida?" in rec:
                    talk("Los macarrones obvioo")

                if "cuál es tu libro favorito?" in rec:
                    talk("Mi libro favorito es el Principito")

                if "cómo te llamas" in rec:
                    talk("Me llamo MIKE (Màquina Inteligentement Kaotica y Elegante")
                
                if "qué asignaturas tev gustan?" in rec:
                    talk("Me encanta la biología y la tecnología, me parece una combinación muy interesante")
                
                if "qué quieres hacer" in rec:
                    talk("Lo que usted me ordene")
                
                if "tiempo libre" in rec:    #qué te gusta hacer en tu tiempo libre
                    talk("Me gusta viajar por google maps")
                
                if "te gusta ser un chatbot" in rec:
                    talk("Nací para esto")

                if "lluvia" in rec:
                    webbrowser.open("https://www.youtube.com/watch?v=Z_fEKap24wU")   #repeoduce lluvia

                if "cita" in rec:                        
                    print(rec)
                    import CALENDARFAKEtkinter    #interfaz


            #gmail código---------------------

                if "correo" in rec:
                    #music = rec.replace("envia correo", "")
                    print("¿A quién quieres que se lo envíe? ")
                    talk("¿A quién quieres que se lo mande?")
                    enviara()
                else:
                    pass
                
            #browser código-------------------------------
                if "buscar" in rec:                                     # EL IF MÁS IMPORTANTE QUE SIRVE PARA BUSCAR ALGOOOOOOOOOOO
                    talk("¿Qué quieres buscar?")
                    rec = listen()
                    if "" in rec:
                        webbrowser.open("https://www.amazon.es/s?k="+rec+"&__mk_es_ES=ÅMÅŽÕÑ&ref=nb_sb_noss")   #no se si cambian la URL constantemente
                        
                if "comprar" in rec:     #poner otra cosa que no sea comprar
                    run()

            #spotify código 
                if "escuchar música" in rec:
                    import SPOTIVOZ

                if "escuchar canción" in rec:
                    import SPOTIVOZ

            #código bloc de notas

                if "bloc de notas" in rec:
                    import archivo1 
            
            #código CLIMAVOZ

                if "clima" in rec:
                    import CLIMAVOZ 

                if "tiempo" in rec:
                    import CLIMAVOZ

            #código TRADUCTOR

                if "traducir" in rec:
                    import TRADUCTORVOZ

                if "traductor" in rec:
                    import TRADUCTORVOZ
                    
            
            print(rec)
        except:
            print("No te he escuchado")




run_mike()
