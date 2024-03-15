# need? 
# communication b/w multiple threads

# acquire(): acquire lock
# release()
# wait(timeout=0) - used to block the thread.
# notify():wake up one thread
# notify_all(): wake up multiple thread

# these methods are called only when lock is acquired

import threading
import time


def write_data():
    con.acquire()
    with open('report.txt', 'w') as file1:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            temp = input(f"Enter the temperature for {day}")
            file1.write(temp+"\n")
        con.notify_all()
        con.release()


def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r') as file1:
        data=file1.readlines()
        max1=float(data[0].strip("\n"))
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > max1:
                max1 = temp
        print("Maximum temperature is", max1)
        con.release()

def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt', 'r') as file1:
        data=file1.readlines()
        sum1 = 0
        
        for temp in data:
            temp = float(temp.strip("\n"))
            sum1 = sum1+temp
        avg = sum1/len(data)
        print("avg temperature is", avg)
        con.release()

con = threading.Condition()

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)
t1.run()
t2.run()
t3.run()