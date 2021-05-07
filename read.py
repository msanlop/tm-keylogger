import pickle
# from collections import deque

test = pickle.load(open("test.p", "rb"))
for i in test:
    print(i)