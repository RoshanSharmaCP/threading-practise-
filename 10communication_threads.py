# threads communicate using signals

# 3 ways of communication

#  - by creating event object(for communication between two threads using flag) - thread2 waits until gets a signal thread1 is completed
#  - by creating conditional object
#  - by using queue module

# import threading
# import time

# e = threading.Event()

# def task():
#     print("thread1 started")
#     time.sleep(3)
#     e.set()
# # set flag to true
    
# def end():
#     e.wait()
#     if e.is_set():
#         print("code for thread 2")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=end)

# t1.start()
# t2.start()


# example2

import threading
from time import sleep

e = threading.Event()

def light_switch():
    while True:
        print("light is green")
        e.set()
        sleep(5)
        print("light is red")
        e.clear()
        sleep(5)
        e.set()

def traffic_message():
    e.wait()
    while e.is_set():
        print("you can go!")
        sleep(0.5)
        e.wait()

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()
