# wakeword.py
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
from jarvis2 import jarvis

model = Model("vosk-model-small-en-in-0.4")  # Ensure path is correct
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def start_listening():
    print("🔊 Listening for wake word: 'jarvis'...")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if "jarvis" in result.get("text", ""):
                    print("🎤 Wake word detected!")
                    jarvis()
                    break
