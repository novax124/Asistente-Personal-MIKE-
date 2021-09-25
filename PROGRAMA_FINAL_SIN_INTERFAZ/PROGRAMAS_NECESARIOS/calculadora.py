import speech_recognition as sr
import pyttsx3

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
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)


    except:
        pass
    return rec

def run_mike8():  #importar esta función para la interfaz gráfica
    
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]
    contador = 0
    coma = ","
    num1 = ""
    num2 = ""

    talk("Te escucho")
    rec = listen()


    if "+" in rec:
        for i in rec: 
            if i in numeros:
                if contador == 0:
                    if i == ",":
                        num1 += "."
                    else:
                        num1 += i
                        print("Num 1 = ", num1)
       
                else:
                    if i == ",":
                        num2 += "."
                    else:
                        num2 += i
                        print("Num 2 = ", num2)
                    
            else:
                contador += 1
        
        print(float(num1) + float(num2))
        talk(float(num1) + float(num2))



    if "menos" in rec:
        for i in rec: 
            if i in numeros:
                if contador == 0:
                    if i == ",":
                        num1 += "."
                    else:
                        num1 += i
                        print("Num 1 = ", num1)
       
                else:
                    if i == ",":
                        num2 += "."
                    else:
                        num2 += i
                        print("Num 2 = ", num2)
                    
            else:
                contador += 1
        
        print(float(num1) - float(num2))
        talk(float(num1) - float(num2))



    if "x" in rec:
        for i in rec: 
            if i in numeros:
                if contador == 0:
                    if i == ",":
                        num1 += "."
                    else:
                        num1 += i
                        print("Num 1 = ", num1)
       
                else:
                    if i == ",":
                        num2 += "."
                    else:
                        num2 += i
                        print("Num 2 = ", num2)
                    
            else:
                contador += 1
        
        print(float(num1) * float(num2))
        talk(float(num1) * float(num2))



    if "*" in rec:
        for i in rec: 
            if i in numeros:
                if contador == 0:
                    if i == ",":
                        num1 += "."
                    else:
                        num1 += i
                        print("Num 1 = ", num1)
       
                else:
                    if i == ",":
                        num2 += "."
                    else:
                        num2 += i
                        print("Num 2 = ", num2)
                    
            else:
                contador += 1
        
        print(float(num1) * float(num2))
        talk(float(num1) * float(num2))



    if "entre" in rec:
        for i in rec: 
            if i in numeros:
                if contador == 0:
                    if i == ",":
                        num1 += "."
                    else:
                        num1 += i
                        print("Num 1 = ", num1)
       
                else:
                    if i == ",":
                        num2 += "."
                    else:
                        num2 += i
                        print("Num 2 = ", num2)
                    
            else:
                contador += 1
        
        print(float(num1) / float(num2))
        talk(float(num1) / float(num2))


run_mike8()