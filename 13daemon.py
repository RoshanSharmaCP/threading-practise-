from threading import *
from time import sleep


def syntax_highlighting():
    for i in range(10):
        print("syntax highlighting")
        sleep(1)

t1 = Thread(target=syntax_highlighting)
t1.daemon = True
t1.start()

sleep(3)
print("close the application")