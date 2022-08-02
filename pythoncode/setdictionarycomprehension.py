"""s=set(range(1,10))
print(s)"""
list_num=list(range(1,11))
set_num={var for var in list_num if var%2==0}
print(set_num)
l1=list(range(1,11))
l2=list(range(11,21))
dloop={}
for i in range(len(l1)):
    dloop[l1[i]]=l2[i]
print(dloop)    
newd={key:value for key,value in zip(l1,l2)}
print(newd)
for x in zip(l1,l2):
    print(x)

