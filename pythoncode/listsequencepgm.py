list_arb=[1,2,3,(5,6),[7,9]]
print(list_arb)
newl=["sequenjc"]
print(newl)
newll=list("sequence")
print(newll)
newlll=[1,2,3,4,5,
 6,7,]
for i in newlll:
    print(i)
new4=[1,3,4,5,6]
print(new4)
new4.clear()
print(new4)
del new4
new4=[2,4,5,5,5]
print(new4[0])
print(new4[-5])
print(new4[0:4])
print(new4[-7:-1])
print(len(new4))
print(new4.count(5))
print(new4.index(4))
print(new4.index(5))
l=[1,2,3,4]
l.append(10)
print(l)
l.insert(1,100)
print(l)
l.insert(100,200)
print(l)
l.insert(-100,300)
print(l)
l1=[1,2,3,4]
l2=[500,600]
l1.extend(l2)
print(l1)
l2.extend(l1)
print(l2)
print(l2.remove(500))
print(l2)