"""
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello! This is a text to speech example.")
engine.runAndWait()

from gtts import gTTS
import os
tts = gTTS("Namaste! Welcome to your custom TTS app.", lang='en')
#tts=gTTS("नमस्ते! कैसे हो?", lang='hi')  # Hindi

tts.save("output.mp3")
os.system("start output.mp3")  # Windows: play audio

"""
import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

# ❌ REMOVE or guard this
# speak()

# ✅ Optional, safe to keep:
"""if __name__ == "__main__":
    speak("Hello! This is a test of the text-to-speech system.")"""






