from collections import ChainMap
d1={'a':1,'b':2}
d2={'b':3,'d':4}
d3={'e':5,'c':6}
c=ChainMap(d1,d2,d3)
print(c)
print(c.maps)
print(list((c.keys())))
#print(type(c.keys()))
print(list(c.values()))
d4={'k':9,'m':7}
c1=c.new_child(d4)
print(c1)
print(c1.maps)
print(c1['b'])
c1.maps=reversed(c1.maps)
print(c1.maps)
print(c1['b'])
