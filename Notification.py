import os 
from winotify import Notification, audio  
from os import getcwd

icon_path=r"C:\Users\offic\OneDrive\Desktop\Open_Skill\jarvisproject\image.png"
toast=Notification(
    app_id="OPEN SKILL",
    title="Alert",
    msg="Attention Here",
    duration="long",
    icon=icon_path
)
toast.set_audio(audio.Default,loop=False)
toast.add_actions(label="click me", launch="https://www.google.com")
toast.show()


