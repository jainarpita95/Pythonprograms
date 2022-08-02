g=(x*x for x in range(10))#0000000))
print(g)
for var in g:
    print(var,end=" ")

print(type(g))
print(next(g))
print(next(g))
print(next(g))
def first_nval(num):
    n=1
    while n<=num:
        yield n
        n=n+1
values=first_nval(1000000000)
print(type(values))
print(next(values))
print(next(values))
print(next(values))
for x in values:
    print(x,end=",")
