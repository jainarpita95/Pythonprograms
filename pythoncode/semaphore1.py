from threading import *
"""import time
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(5):
        print("good evenong:",end='')
        time.sleep(1)
        print(name)
    s.release()
t1=Thread(target=wish,args=("dhoni",))
t2=Thread(target=wish,args=("yuvraj",))
t3=Thread(target=wish,args=("kholi",))
t1.start()
t2.start()
t3.start()"""
"""s=Semaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("end")
s=BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("end")"""

