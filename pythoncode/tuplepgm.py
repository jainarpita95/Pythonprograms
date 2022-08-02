t=10,20,30#parenthesis are optional
print(t)
t1=(91,2,3)
print(t1)
t3=tuple([1,2,45,67,3,3,3,6])
print(t3)
tu=(9,)#,is important to declare single tuple else it will considerd as integer
print(type(tu))
tup=(9)
print(type(tup))
print(len(t3))
t3.count(3)
t3.index(67)
min(t3)
max(t3)
sort_t3=sorted(t3)
print(sort_t3)
a=20
b=30
c=40
d=50
t5=a,b,c,d #packing a tuple variable to tuple
print(a,b,c,d,t5)
#unpacking tuple
#note for unpacking no of element in tuple should be equal to assigning variable
t6=30,50,70,80
a,b,c,d=t6
print(a,b,c,d,t6)
