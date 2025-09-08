# auto_main_brain.py
from web_open import open_web
from play_music_on_youtube import play as play_yt
from play_music_on_spotify import splay as play_spotify
from stt import speak
from Search import search_any
import pyautogui  as gui
import time
from check_network import internet_status

internet_status()

def auto_main_brain(text):
    text = text.lower()

    if any(word in text for word in ["open", "launch", "website", "start"]):
        open_web(text)

    elif "play music" in text or "youtube" in text or "play song" in text:
        query = text.replace("play on youtube", "").replace("youtube", "").replace("play music", "").replace("play song", "").strip()
        speak("which song do you want to play")
        s=input("Song_Name:")
        speak(f"Playing {s} song on YouTube.")
        play_yt(s)

    elif "play on spotify" in text or "spotify" in text:
        query = text.replace("play on spotify", "").replace("spotify", "").strip()
        speak(f"Playing {query} on Spotify.")
        play_spotify(query)

    elif "battery" in text or "charging" in text:
        from battery import battery_alert
        from threading import Thread
        speak("Starting battery monitoring.")
        Thread(target=battery_alert, daemon=True).start()

    elif "exit" in text or "quit" in text:
        speak("Shutting down Jarvis.")
        exit()


    elif "weather" in text:
        from weather_module import get_weather
        speak(get_weather("Meerut"))

    elif "news" in text:
        from news_module import get_news
        speak(get_news())   

    elif "check internet speed" in text or "net speed " in text or "check dowload speed" in text or "upload speed" in text:
        if text=="check dowload speed":
             from check_internet_speed import get_internet_speed
             get_internet_speed()
        else:
            from check_int import run_test
            run_test()
            
    elif text.startswith("search"):
        text = text.replace("search", " ")  # Remove "search" keyword
        text = text.strip()  # Clean extra whitespace
        search_any(text)  # Function to handle search
        time.sleep(0.5)
        gui.press("enter")  # Simulate Enter key

    else:
        speak("Sorry, I didn't understand that.")


  
while True:
    x=input("data:")
    auto_main_brain(x)

# filepath: c:\Users\offic\OneDrive\Desktop\New folder\private\jarvisproject\auto_main_brain.py

# ...existing code...

"""if __name__ == "__main__":
    x = input("data:")"""
    # Add any other code that should only run when executed directly