 #how memory manage in python
"""import threading
print("current executing thread:",threading.current_thread().name)"""
from threading import *
#print("current thread:",Thread.current_thread().name).wrong :error coming
def display():
    for i in range(1,11):
        print("childthread")
t=Thread(target=display)
t.start()
#t.join()
for i in range(1,11):
    print("main thread")

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("childthread1")
t=MyThread()
t.start()
for i in range(5):
    print("mainthread1")
