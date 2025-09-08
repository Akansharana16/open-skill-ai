#import open_app    #locate the folder    #locate the folder

import pyautogui as ui
import stt
from play_music_on_youtube import play
from play_music_on_spotify import splay
import web_open

def close():
    ui.hotkey('alt', 'f4')  # corrected casing

def auto_main_brain(text):
    text = text.lower().strip()

    if text.startswith("open"):
        web_open.open_web(text)

    elif "close" in text:
        close()

    elif "play music on youtube" in text:
        stt.speak("Which song do you want to play?")
        s=input(" ")
        play(s)

    elif "play music on spotify" in text:
        stt.speak("Song name for Spotify: ")
        song = input(" ")
        splay(song)

    elif text.startswith("play music"):
        song = text.replace("play music", "").strip()
        if song:
            play(song)
        else:
            stt.speak("Which song do you want to play : ")
            song = input(" ")
            play(song)

    elif text.startswith("play spotify"):
        song = text.replace("play some music", "").strip()
        if song:
            splay(song)
        else:
            stt.speak("Which song do you want to play : ")
            song = input(" ")
            splay(song)

    else:
        print("Sorry, command not recognized.")
        stt.speak("Sorry, command not recognized")

# ✅ Main program loop
"""while True:
    x = input("Asking.....: ")
    if x.lower() in ["exit", "quit", "stop"]:
        break
    auto_main_brain(x)"""




"""
import pyautogui as ui
import stt
from play_music_on_youtube import play
from play_music_on_spotify import splay
from web_open import open_web        
def auto_main_brain(text):
    text = text.lower().strip()
    if text.startswith("open"):
        open_web(text)  

    elif "play music" in text or "play music on youtube" in text:  
        stt.speak() 
        play(x)  
        #stt.listen(x)   
    elif "play some music" in text or "play music on spotify" in text:        
        stt.speak() 
        splay(x)   
        #stt.listen(x)
    else:
        pass

while True:
    x = input("Asking.....: ")
    if x.lower() in ["exit", "quit", "stop"]:
        break
    auto_main_brain(x)

""" 