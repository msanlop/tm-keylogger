from pynput import keyboard
import time
from collections import UserDict, deque
from event import KeyEvent
import pickle

keyTimes = {
}
keyEventDeque = deque()
t0 = time.time()

record = False


def on_press(key):
    global record
    global t0
    try:
        if key == keyboard.Key.delete:
            t0 = time.time()
            record = True
        elif keyTimes.get(key, 0) <= 0 and record:
            keyTimes.update({key:time.time()})
    except Exception as e:
        print("error on press", e)
    

def on_release(key):
    try:
        if not record:
            return
        t1 = time.time() - t0
        dt = time.time() - keyTimes.get(key)
        keyTimes.update({key:0})
        keyEventDeque.append(KeyEvent(key, t1, dt))
        print(t1)
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            for i in keyEventDeque:
                print(i)
            pickle.dump(keyEventDeque, open("test.p", "wb"))
            # Stop listener
            return False
    except Exception as e:
        print("Error", e)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()