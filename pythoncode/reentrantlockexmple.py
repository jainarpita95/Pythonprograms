from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    time.sleep(0.5)
    print(result)
#def results(n):
   # print("the factorial of",n,"is",factorial(n))
t1=Thread(target=factorial,args=(5,))
t2=Thread(target=factorial,args=(9,))
t1.start()
t2.start()
