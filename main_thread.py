# Python interpreter request OS for creating one thread called as Main thread
# main thread is created by python virtual machine

# threads are python objects of threading.Thread() class
import threading

print(threading.current_thread()) 
print(threading.current_thread().is_alive()) 