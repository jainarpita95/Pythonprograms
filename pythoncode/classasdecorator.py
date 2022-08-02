"""class MyDecorator:
    def __init__(self,function):
        self.function=function
    def __call__(self,*args):
        print("*"*10)
        self.function(*args)
        print("*"*10)
@MyDecorator
def function(name):
    print(name)
function('arpita')"""
#2nd program
class CheckDenom:
    def __init__(self,func):
        self.func=func
    def __call__(self,x,y):
        if y==0:
            print("denominator cannot be zero")
            #return print("denominator can not be zero")
        else:
            self.func(x,y)
@CheckDenom
def div_function(a,b):
    print(a/b)
(div_function(9,3))
(div_function(9,0))
        
