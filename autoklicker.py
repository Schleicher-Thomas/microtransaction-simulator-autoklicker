# autoclicker for "Microtransaction-Simulator"
# you need to install python on your computer to run this
# paste this code into an empty file and call it autoklicker.py
# to run the file you have to run type "autoklicker.py" into your Windows terminal and then press 'w'
# the button coordinates are coded for your primary monitor to have 1080p
# you can adjust the button coordinates below
# to find you own coordinates you can just make a screenshot of the game and open it in paint
# the current mouse coordinates are displayed in the bottom left corner

import time
import threading

# install pynput in cmd (windows console) with:  pip install pynput

from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="w")

clicking = False
mouse = Controller()



def clicker():
    #n = 4
    while True:
        if clicking:
            mouse.position = (900,1000) #new cards
            mouse.click(Button.left, 1)
            time.sleep(0.01)

            mouse.position = (700,400) #open 1
            mouse.click(Button.left, 1)
            time.sleep(0.01)

            mouse.position = (900,400) #open 2
            mouse.click(Button.left, 1)
            time.sleep(0.01)

            mouse.position = (700,600) #open 3
            mouse.click(Button.left, 1)  
            time.sleep(0.01)

            mouse.position = (900,600) #open 4
            mouse.click(Button.left, 1)
            time.sleep(0.01)

            print(".")
            #n=n-1
        time.sleep(0.01)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
