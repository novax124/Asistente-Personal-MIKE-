import webbrowser

resp = input("Hola ¿Qué quieres buscar?: ")

if "noticias" in resp:
    webbrowser.open('https://www.lavanguardia.com/')


if "YouTube" in resp:
    webbrowser.open("https://www.youtube.com")
    
if "Amazon" in resp:
    resp = input("¿Quieres comprar algo en específico?: ")
    if "" in resp:
        webbrowser.open("https://www.amazon.es/s?k="+resp+"&__mk_es_ES=ÅMÅŽÕÑ&ref=nb_sb_noss_2")
    else:
        webbrowser.open("https://www.amazon.es/")

if "Wikipedia" in resp:
    resp = input("¿Qué quieres buscar?: ")
    if "" in resp:
        webbrowser.open("https://es.wikipedia.org/wiki/"+resp)
    else:
        pass