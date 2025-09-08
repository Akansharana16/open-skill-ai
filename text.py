import pywhatkit as kit
import datetime

now=datetime.datetime.now()
hour=now.hour
minute=now.minute
second=now.second
kit.sendwhatmsg("+919917729442", "hey demo", hour,minute+1)