from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json

model = Model("vosk-model-small-en-in-0.4")  # Download separately
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec = KaldiRecognizer(model, 16000)
    print("Listening for 'jarvis'...")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if "jarvis" in result.get("text", ""):
                print("Wake word detected! 🔥 Starting Jarvis...")
                from jarvis2 import jarvis
                jarvis()
                break
