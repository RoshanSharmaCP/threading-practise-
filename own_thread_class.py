from threading import Thread

l = [1,2,3]

class MyThread(Thread):
    def run(self):
        for item in l:
            print("executed own thread")

t1 = MyThread()
t1.start()
