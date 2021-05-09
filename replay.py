import pickle
from pynput import keyboard
from event import KeyEvent
import time
import sys
# from collections import deque

kController = keyboard.Controller()


events = pickle.load(open(sys.argv[1], "rb"))
for i in events:
    print(i)

def play():
    print("playing sequence...")
    t = time.perf_counter()
    # schedule key presses as tasks
    for event in events:
        while time.perf_counter() - t <= event.time:
            time.sleep(0.000000001)

        if event.action == 'p':
            print(str(event) + " at " + str(time.perf_counter() - t))
            kController.press(event.key)
        else:
            print(str(event) + " at " + str(time.perf_counter() - t))
            kController.release(event.key)
    exit()

time.sleep(2)
play()


#def on_press(key):
#    print(key)
#    if key == keyboard.Key.delete:
#        play()
#        return False

#with keyboard.Listener(
#       on_press=on_press) as listener:
#    listener.join()


