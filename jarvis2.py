from auto_main_brain import auto_main_brain
from orognial import speech_to_text_python
from threading import Thread
#from battery import battery_alert
import os
import time

def check_input():
    output_text = ""
    while True:
        with open("input.txt", "r" ) as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text:
                print("📥 New input detected:", output_text)
                auto_main_brain(output_text)
        time.sleep(1)  # Prevent CPU overuse and allow update timing



# Create input.txt if it doesn't exist
if not os.path.exists("input.txt"):
    with open("input.txt", "w") as file:
        file.write("")

def jarvis():
    t1 = Thread(target=speech_to_text_python)
    t2 = Thread(target=check_input)       
    t1.start()
    t2.start()
    t1.join()
    t2.join()


jarvis()
