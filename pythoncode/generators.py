def sq_numbers(n):
    for i in range(1,n+1):
        yield(i*i)#keyword in python
a=sq_numbers(3)
#print(type(a))
#print(next(a))
#print(next(a))
#print(next(a))
for i in a:
    print(i)
