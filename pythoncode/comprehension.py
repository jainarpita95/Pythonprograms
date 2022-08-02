#listcomprehension
new_list=[x for x in range(1,11)]
print(new_list)
even_list=[x  if x%2==0 else 1000 for x in new_list]
print(even_list)"""
#multiplying elements in the list
"""list_one=[1,2,3]
list_two=[1,2,3,4]
list_one=list(range(1,4,2))
list_two=list(range(1,8,2))
new_list=[list_one[i]+list_two[i] for i in range(len(list_one))]
print(new_list)
#multiplying elements in list
result_list=[i*j for i in list_one for j in list_two]
print("resultlist:",result_list)
#list of list
l1=list(range(1,11,2))
l2=list(range(11,21,2))
print("list1",l1)
print("list2",l2)
print("*"*40)
new_list=[]

for i in l1:
    for j in l2:
        new_list.append([i,j])
print("nested",new_list)
#comprehension
print("*"*40)
new_list2=[[i,j] for i in l1 for j in l2]
print(new_list2)
