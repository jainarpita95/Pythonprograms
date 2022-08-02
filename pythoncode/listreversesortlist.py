l=[1,2,3,4,5,6,7,8,9,1,0,11,22,33,44]
#l.reverse()
#print(l)
#l.sort()
#print(l)
#li=sorted(l)
#print(li)
r_obj=reversed(l)
for r in r_obj:
    print(r)
li=l    
print(id(li),id(l))
l1=l.copy()
print(l1,id(l),id(l1))
