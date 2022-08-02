import time
def doubles(num):
    for n in num:
        time.sleep(1)
        print("double:",2*n)
def squares(num):
    for n in num:
        time.sleep(1)
        print("square:",n*n)
num=[1,2,3,4,5,6]
bgt=time.time()
doubles(num)
squares(num)
print("total time:",time.time()-bgt)
