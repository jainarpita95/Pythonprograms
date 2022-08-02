#create tuple using range function and add all tuple element to a list
t=tuple(range(1,21))
num_list=[]
num_list.extend(t)
print(num_list)
#insert funtion
l=[1,2,3,4,5]
l.insert(2,100)
print(l)
#create one dictionary person_info
thisdict={"name":"tony",
          "age":22,
          "salary":3000,
          "city":"bhopal"}
for key,value in thisdict.items():
    print(key,value,sep="-")
