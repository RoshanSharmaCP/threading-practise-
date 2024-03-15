# its a modified version of RLock to use acquire() mnultiple times
from threading import *

lock = RLock()
class Bus:
    def __init__(self, name, available_seats, rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock
    def reserve(self, need_seats):
        self.rlock.acquire()
        self.rlock.acquire()
        print("Available seats are", self.available_seats)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats available")
        self.rlock.release()
        self.rlock.release()


b1 = Bus("ABC travels",2, lock)
t1 = Thread(target=b1.reserve, args=(2,), name="Jay")
t2 = Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()
