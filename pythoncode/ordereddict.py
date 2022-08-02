from collections import OrderedDict
print("before:\n")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key,value in od.items():
    print(key,value)
print("\nAfter:\n")
od['c']=5
for key,value in od.items():
    print(key,value)
print("\n")   
"""d={}
d[1]=1
d[2]=2
d[3]=3
d[4]=4
print("\n")
for x,y in d.items():
    print(x,y)
d[3]=5
print("\n")
for x,y in d.items():
    print(x,y)"""
#pop
od.pop('c')
for key ,value in od.items():
    print(key,value)
print("\nAfter re-insertin\n")
od['c']=3
for key , value in od.items():
    print(key,value)
