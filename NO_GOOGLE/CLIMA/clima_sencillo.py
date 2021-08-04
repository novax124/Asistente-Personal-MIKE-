import requests
from pprint import pprint

city = input("Enter your city:  ")
url = "api url".format(city) #https://openweathermap.org

res = requests.get(url)

data = res.json()


temp = data["main"]["temp"]
vel_viento = data["wind"]["speed"]

latitud = data["coord"]["lat"]
longitud = data["coord"]["lon"]

descripcion = data["weather"][0]["description"]

print("Tempreratura: ", temp)
print("Velocidad del viento: {} m/s".format(vel_viento))
print("Latitud: {}".format(latitud))
print("Longitud: {}".format(longitud))
print("Descripción: {}".format(descripcion))

