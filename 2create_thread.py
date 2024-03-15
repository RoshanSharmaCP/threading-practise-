from threading import Thread, current_thread

def display(n, msg):
    print("t1 thread details", current_thread())
    for i in range(n):
        print(msg)

    
# t1 = Thread(target = display)
t1 = Thread(target = display, kwargs={'n': 4, 'msg': "Hello"})
# when Thread object is craeted then the thread is created in new memory but the execution will only start once start() is trigger
t1.start()

# when start() is called then internally run() function inside Thread class is called

for i in range(5):
    print("Main thread running")

