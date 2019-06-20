import os 
import time
import curses
from playsound import playsound

timeout=60*5 #timeout in seconds

def human_time(seconds):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(seconds))
    


path ="../workspace.md"
last_mod_time=0
while True:
    time.sleep(timeout)
    this_mod_time = os.path.getmtime(path)
    if this_mod_time == last_mod_time:
        print "No changes, bastard!" 
        playsound('sonicdrowing_01.wav') 
    last_mod_time=this_mod_time
    last_mod_time = os.path.getmtime(path)



