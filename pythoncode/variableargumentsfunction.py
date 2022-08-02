#*args function
def num_add(*args):
    print(type(args))
    for i in args:
        print(i)
num_add(1,2)
num_add(1,2,3)
#varable number of key arguments
def show_num(**kargs):
    print(type(kargs))
    for x,y in kargs.items():
        print(x,"=",y)
show_num(num1=100,num2=20)
