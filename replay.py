import pickle
from pynput import keyboard
from collections import deque
from event import KeyEvent
import asyncio
import time
import sys
# from collections import deque

kController = keyboard.Controller()

loop = asyncio.get_event_loop()

events = pickle.load(open(sys.argv[1], "rb"))
for i in events:
    print(i)

async def play():
    tasks = []
    print("playing sequence...")
    t = time.time()
    # schedule key presses as tasks
    while len(events)> 0:
        elem = events.popleft()
        tasks.append(asyncio.create_task(pressKey(elem)))

    await asyncio.gather(*tasks)
        

async def pressKey(event):
    await asyncio.sleep(event.time)
    kController.press(event.key)
    await asyncio.sleep(event.dt)
    kController.release(event.key)

def on_press(key):
    print(key)
    if key == keyboard.Key.delete:
        # loop.run_until_complete(play())
        return False

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

loop = asyncio.get_event_loop()

loop.run_until_complete(play())


