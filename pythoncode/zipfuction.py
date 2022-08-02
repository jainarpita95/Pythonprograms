# zip on list
l1=[1,4,2,7]
l2=[5,1,7,4]
t=zip(l1,l2)
print(type(t))
for x in t:
    print(x)
print("$"*50)
# zip on dictionaries
d1={1:2,3:4}
d2={5:6,7:8}
g=zip(d1,d2)
for y in g:
    print(y)
print("$"*50)
#zip function on tuple
t1=(3,4,6)
t2=(8,9,4)
h=zip(t1,t2)
for j in h:
    print(j)
print("&"*50)
#zip on set
s1={3,4,5}
s2={4,8,0}
u=zip(s1,s2)
for j in u:
    print(j)
