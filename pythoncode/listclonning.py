import copy
l1=[1,2,[3,4],5]
l2=copy.copy(l1)
#l1.append(999)
#print(l1,l2)
#l1[2].append(333)
#print(l1,l2)
l3=copy.deepcopy(l1)
l1.append(999)
print(l1,l3)
l1[2].append(333)
print(l1,l3)
