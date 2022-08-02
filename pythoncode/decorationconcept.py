"""def check_denom(function_name):
    def inner(a,b):#here decor function should have same number of arguments as of wrapped function.
        if b==0:
            print("denominator should not be zero")
        else:
            function_name(a,b)
    return inner
@check_denom
def div_function(x,y):
    print(x/y)
div_function(12,3)          
div_function(12,0)"""
def decor_function(input_function):
    def inner():
        print("#"*10)
        print("decoration with flowers")
        input_function()
        print("#"*10)
    return inner
@decor_function
def old_function():
    print("no decoration")
old_function()
#function without @decor
def decor_function():
    def inner(input_function):
        print("#"*10)
        print("decoration with flowers")
        input_function()
        print("#"*10)
    return inner
def old_function():
    print("no decoration")
return_function=decor_function()
return_function(old_function)



