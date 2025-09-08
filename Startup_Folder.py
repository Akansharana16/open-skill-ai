import os
import shutil

def add_to_startup():
    startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script = os.path.abspath("gui_launcher.pyw")  # Or .exe path
    shortcut = os.path.join(startup_dir, "Jarvis.lnk")
    if not os.path.exists(shortcut):
        shutil.copy(script, startup_dir)