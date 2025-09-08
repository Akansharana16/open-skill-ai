import tkinter as tk
from threading import Thread
from wakeword import start_listening

def run_jarvis():
    Thread(target=start_listening).start()

app = tk.Tk()
app.title("JARVIS Control Panel")
app.geometry("400x200")
app.configure(bg="black")

tk.Label(app, text="🎙 JARVIS Voice Assistant", font=("Arial", 16), fg="cyan", bg="black").pack(pady=20)
tk.Button(app, text="Start Listening", font=("Arial", 14), command=run_jarvis, bg="green", fg="white").pack(pady=10)
tk.Button(app, text="Exit", font=("Arial", 14), command=app.quit, bg="red", fg="white").pack(pady=5)

app.mainloop()

