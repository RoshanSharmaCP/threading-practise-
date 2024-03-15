# is_alive(): to check if thread is running
# main_thread(): returns main threads details
# active_count(): number of running threads
# enumerate(): list of all running threads with details
# get_native_id(): know native id of thread. Native id is provided by OS, thread_id is provided by python interpreter


from threading import Thread, current_thread, main_thread, enumerate, active_count, get_native_id

def display():
    print("native id of t1", get_native_id())
    print("main thread details", main_thread())
    print("t1 thread details", current_thread())
    for i in range(4):
        print("display func")

t1 = Thread(target = display)
print("before", t1.is_alive())
print("before t1, number of threads", active_count())
t1.start()
print("after t1, number of threads", active_count())
print("after", t1.is_alive())

print("......", enumerate())

print("native id of MAIN THREAD", get_native_id())