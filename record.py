from pynput import keyboard
import time
from collections import UserDict, deque
from event import KeyEvent
import pickle

keyTimes = {
}
keyEventDeque = deque()
t0 = 0
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
        t1 = keyTimes.get(key) - t0
        dt = time.time() - keyTimes.get(key)
        keyEventDeque.append(KeyEvent(key, t1, dt))
        keyTimes.update({key:0})
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            newDeque = sortDeque(keyEventDeque)
            for i in newDeque:
                print(i)
            pickle.dump(newDeque, open("sequence.p", "wb"))
            # Stop listener
            return False
    except Exception as e:
        print("Error", e)

def sortDeque(d):
    copy = d.copy()
    l = deque()
    min = KeyEvent(keyboard.Key.enter, 999999999999,99999999999)
    while len(copy) > 0:
        for i in copy:
            if i.time < min.time:
                min = i
        l.append(min)
        copy.remove(min)
        min = KeyEvent(keyboard.Key.enter, 999999999999,99999999999)
    return l
    

        

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()