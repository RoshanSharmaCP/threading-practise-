# benefits:
# thread race condition handled internally within queue module
# implemented all the required locking semantics
from time import sleep
from threading import Thread
from queue import Queue

def producer(my_que):
    print("Producer running")
    n = int(input("Enter number of students"))
    for i in range(n):
        marks = float(input("Enter marks"))
        my_que.put(marks)
    my_que.put(None)

def consumer(my_que):
    print("consumer running")
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f"got {item}")
    print("Consumer:end")

my_que = Queue()
t1 = Thread(target=producer, args=(my_que,))
t2 = Thread(target=consumer, args=(my_que,))

t1.start()
t2.start()

