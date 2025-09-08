import psutil
import time
import platform
import os
from plyer import notification
from playsound import playsound
from stt import speak

SOUND_FILE = "alert.mp3"  # Replace with your actual sound file path

def play_sound():
    try:
        playsound(SOUND_FILE)
    except Exception as e:
        print("Error playing sound:", e)

def shutdown():
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 1")
    elif system == "Linux" or system == "Darwin":
        os.system("shutdown now")
    else:
        print("Shutdown not supported on this OS.")

def battery_alert():
    while True:
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        plugged = battery.power_plugged

        # Notify full battery
        if percent == 100 and plugged:
            speak("Battery is 100%. Unplug the charger.")
            notification.notify(
                title="🔋 Battery Full",
                message="Battery is 100%. Unplug the charger.",
                timeout=5
            )
            play_sound()

        # Warn low battery (below 20%)
        elif percent <= 20 and not plugged:
            speak(f"Battery is at {percent}%. Please plug in your charger.")
            notification.notify(
                title="⚠️ Low Battery",
                message=f"Battery is at {percent}%. Please plug in your charger.",
                timeout=5
            )
            play_sound()

        # Shutdown at critical level (below 5%)
        if percent <= 5 and not plugged:
            speak("Battery critical! Shutting down.")
            notification.notify(
                title="💀 Critical Battery",
                message="Battery critical! Shutting down...",
                timeout=5
            )
            play_sound()
            time.sleep(1)
            shutdown()

        # Log info to terminal + speak it
        print(f"Battery: {percent}%, Charging: {plugged}")
        speak(f"Battery {percent} percent")
        speak("Charging" if plugged else "Not charging")

        time.sleep(60)  # Check every minute

