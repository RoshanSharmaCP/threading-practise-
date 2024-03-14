# race condition is a bug generated when two or more threads tries to update the same variable and results into unreliable output

# how to prevent race condition:
#  - prevent concurrent access
#  - using thread synchronization techniques:
#        - using Locks
#        - using R-lock
#        - using semaphores

from threading import *

class Bus:
    def __init__(self, name, available_seats):
        self.available_seats = available_seats
        self.name = name
    def reserve(self, need_seats):
        print("Available seats are", self.available_seats)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats available")


b1 = Bus("ABC travels",2)
t1 = Thread(target=b1.reserve, args=(2,), name="Jay")
t2 = Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()

