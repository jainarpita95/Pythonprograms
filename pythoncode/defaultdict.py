from collections import defaultdict
def just_value():
    return "no value"
#d=defaultdict(just_value)
#using lambda as default_factory
d=defaultdict(lambda:"no value")
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])
print(d.__missing__('a'))
print(d.__missing__('d'))
print("\n\n")
#using list as defult_factory

d1=defaultdict(list)

for i in range(5):
    d1[i].append(i)
print("DIctionary with values as list:")
print(d1)
d1[0]=3
print(d1[1])
print("\n\n")
d2=defaultdict(int)
l=[1,2,3,4,2,4,1,2]
for i in l:
    print(d2[i])
    d2[i]+=1
print(d2)    
