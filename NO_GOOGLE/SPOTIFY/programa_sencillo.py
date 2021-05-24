from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep

# your credentials
client_id = 'Poner id' #https://developer.spotify.com/dashboard/login
client_secret = 'Poner id '
flag = 0

# artist and name of the song
author = ''
song = 'Honeypie'.upper()

if len(author) > 0:
    # authenticate
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = sp.search(author)

    for i in range(0, len(result["tracks"]["items"])):
        # songs by artist
        name_song = result["tracks"]["items"][i]["name"].upper()

        if song in name_song:
            flag = 1
            web.open(result["tracks"]["items"][i]["uri"])
            sleep(5)
            pyautogui.press("enter")
            
# if song by artist not found
if flag == 0:
    song = song.replace(" ", "%20")
    web.open(f'spotify:search:{song}')
    sleep(5)
    for i in range(28):                #saltos para llegar a la canción
        pyautogui.press("tab")

    for i in range(2):
        pyautogui.press("enter")
        sleep(600)