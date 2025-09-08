import os
import threading
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Global flag to stop threads
stop_listening_flag = threading.Event()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def print_loop():
    while not stop_listening_flag.is_set():
        print(Fore.GREEN + " ", end="\r", flush=True)


def translate_hi_to_en(text):
    try:
        return translate(text, "en-us")
    except Exception:
        return "[Translation Failed]"


def speech_to_text_python():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000
    recognizer.pause_threshold = 0.5
    recognizer.non_speaking_duration = 0.3

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(Fore.YELLOW + "Calibrated for ambient noise. You can start speaking...")

        while not stop_listening_flag.is_set():
            try:
                print(Fore.CYAN + "\nclear-speech", end="\r")
                audio = recognizer.listen(source, timeout=10)
                print(Fore.LIGHTBLACK_EX + "Recognizing...", end="\r", flush=True)

                recognized_text = recognizer.recognize_google(audio, language='en-US').strip()  #hi-IN

                if recognized_text:
                    print(Fore.MAGENTA + f"\n You said : {recognized_text}")
                    trans_text = translate_hi_to_en(recognized_text)
                    print(Fore.BLUE + f"Shivank (EN): {trans_text}")

                    with open("input.txt", "w", encoding="utf-8") as file:
                        file.write(trans_text.strip())
                        file.truncate(0)
                else:
                    print(Fore.YELLOW + "\n No clear speech detected.")

            except sr.WaitTimeoutError:
                print(Fore.YELLOW + "\n No speech detected within timeout. Try again...")
            except sr.UnknownValueError:
                print(Fore.RED + "\n Could not understand audio.")
            except sr.RequestError:
                print(Fore.RED + "\n API unavailable or error.")
            except KeyboardInterrupt:
                stop_listening_flag.set()
                print(Fore.RED + "\n Stopped by user.")
                break


def main():
    """Main execution flow: start threads for listening and status output."""
    try:
        clear_console()

        stt_thread = threading.Thread(target=speech_to_text_python)
        print_thread = threading.Thread(target=print_loop, daemon=True)

        print_thread.start()
        stt_thread.start()
        stt_thread.join()
    except KeyboardInterrupt:
        stop_listening_flag.set()
        print(Fore.RED + "\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
