from pynput import keyboard
import time
from collections import UserDict, deque
from event import KeyEvent
import pickle

keyTimes = {
}
keyEventList = []
t0 = 0
record = False


def on_press(key):
    global record
    global t0
    try:
        if key == keyboard.Key.delete:
            t0 = time.perf_counter()
            record = True
            keyEventList.append(KeyEvent(key, 0, 'p'))
        elif keyTimes.get(key, True) and record:
            keyTimes.update({key:False})
            keyEventList.append(KeyEvent(key, time.perf_counter() - t0, 'p'))

    except Exception as e:
        print("error on press", e)
    

def on_release(key):
    global t0
    try:
        if not record:
            return
        # t1 = keyTimes.get(key) - t0
        # dt = time.time() - keyTimes.get(key)
        keyEventList.append(KeyEvent(key, time.perf_counter() - t0, 'r'))
        keyTimes.update({key:True})
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # newDeque = sortDeque(keyEventDeque)
            for i in keyEventList:
                print(i)
            pickle.dump(keyEventList, open("sequence.p", "wb"))
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
