# thread synchronization ensures that two or more threads do not access simultaneously certain code segment known as critical section

# threading module provides a Lock class to deal with race condition
# Lock has two states:

# ## Locked: the lock acquired by one thread using acquire() function in lock class in critical section and after the work has been completed the thread release the lock using release function in lock class
# ## Unlocked: when this is the status of critical section provided by Lock class then lock can be acquired by any other thread

# acquire() method syntax:
# lock_object.acquire([blocking=True], timeout=-1)


# from threading import *
# from time import sleep

# mylock = Lock()
# def task(mylock, msg):
#     mylock.acquire()
#     for i in range(4):
#         print(msg)

#     sleep(3)
#     mylock.release()

# t1 = Thread(target=task, args=(mylock, "thread t1 running"))
# t2 = Thread(target=task, args=(mylock, "....thread t2 running"))
# t1.start()
# t2.start()

# solution to previous race condition

from threading import *

lock = Lock()
class Bus:
    def __init__(self, name, available_seats, l):
        self.available_seats = available_seats
        self.name = name
        self.l = l
    def reserve(self, need_seats):
        self.l.acquire()
        print("Available seats are", self.available_seats)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats available")
        self.l.release()


b1 = Bus("ABC travels",2, lock)
t1 = Thread(target=b1.reserve, args=(2,), name="Jay")
t2 = Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()

# two acquire or release functions can't be used using Lock
