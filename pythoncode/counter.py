from collections import Counter
a=Counter("mississipi")
for i in a.elements():
    print(i,end=' ')
print()    
b=Counter({'geeks':4,'for':1,'gif':2,'python':3})
for i in b.elements():
    print(i,end=' ')
print()    
c=Counter([1,2,5,2,5,6,4,2,5,6,7,8,7])
for i in c.elements():
    print(i,end=' ')
print()    
d=Counter(a=2,b=3,c=6,g=7,h=4,e=5)
for i in d.elements():
    print(i,end=' ')
