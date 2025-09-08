import pyautogui as gui
import time


def search_any(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)
