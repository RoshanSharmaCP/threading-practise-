from threading import *

l=RLock()
def get_first_line():
    l.acquire()
    print("Code for fetching first line")
    l.release()

def get_second_line():
    l.acquire()
    print("code for fetching second line")
    l.release()

def main():
    l.acquire()
    get_first_line()
    get_second_line()
    l.release()

t1 = Thread(target=main)
t1.start()