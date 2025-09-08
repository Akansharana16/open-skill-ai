import webbrowser
import psutil

youtube_open = False

def play(text):
    global youtube_open
    text = text.lower()

    if "stop" in text and "youtube" in text:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            try:
                pname = proc.info['name'].lower() if proc.info['name'] else ""
                if "chrome" in pname or "msedge" in pname or "firefox" in pname:
                    proc.kill()
                    youtube_open = False
                    print("✅ Closed YouTube browser.")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return "Stopped YouTube."

    elif "youtube" in text and not youtube_open:
        query = text.replace("youtube", "").strip().replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        youtube_open = True
        return f"🎵 Opening YouTube for {query}..."

    elif youtube_open:
        return "▶️ YouTube is already open."

    else:
        return "⚠️ I didn't understand your YouTube command."


# ===========================
# Jarvis main loop
# ===========================
if __name__ == "__main__":
    print("🤖 Jarvis is ready! (type your command, 'exit' to quit)\n")
    while True:
        command = input("You: ")

        if command.lower() == "exit":
            print("👋 Goodbye, master!")
            break

        response = play(command)
        print("Jarvis:", response)






"""import pywhatkit as pw


def play(text):
    pw.playonyt(text)"""

# ❌ REMOVE:
"""
def play(text):
    pw.playonyt(text)
while True:
    x=input("song name :") 
    play(x)   """


