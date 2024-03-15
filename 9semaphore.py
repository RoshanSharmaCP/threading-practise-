# in lock and rlock, at a time only one thread is allowed to execute
# semaphore is used to limit the access to the shared resources with limited capacity
# maximum 3 threads allowed to execute the critical section

from threading import *
import time

obj = Semaphore(2)

def display(name):
    obj.acquire()
    for i in range(3):
        print("hello")
        print(name)
        time.sleep(0.5)
    obj.release()

t1 = Thread(target=display, args=('Thread 1', ))
t2 = Thread(target=display, args=('Thread 2', ))
t3 = Thread(target=display, args=('Thread 3', ))
t4 = Thread(target=display, args=('Thread 4', ))
t5 = Thread(target=display, args=('Thread 5', ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()