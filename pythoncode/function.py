def add_fun(a,b):
    """this is add fun"""
    print(f"sum of a and b is {a+b}")
    
print(add_fun.__doc__)    
add_fun(100,200)
#print(help(add_fun))

#global and local variable
x=100
def add_fun():
    print(f"x is global variable{x}")
    global a
    a=100
#print(a)
#def print_a():
    #global a
    #print(a)


#returing other function in fuction
def print_message():
    def wish_message(msg):
        print("your message is:",msg)
    return wish_message
return_value=print_message()
print(return_value)
print(type(print_message))
return_value("hi how are u")


