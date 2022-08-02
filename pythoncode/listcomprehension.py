list_one=list(range(1,11,2))
list_two=list(range(11,21,2))
new_list=[list_one[i]*list_two[i] for i in range(len(list_one))]#elements eiher should be same 
print(new_list)
print("$"*40)
#multiplying elements in list
result_list=[i*j for i in list_one for j in list_two]#no need of elements should be same
print("resultlist:",result_list)
print("$"*40)
#nested list#no need of element should be same
nest_list=[[i,j] for i in list_one for j in list_two]
print(nest_list)
#list to dict for loop
dict_loop={}
for i in range(len(list_one)):
    dict_loop[list_one[i]]=list_two[i]#element should be same else error out of index
print(dict_loop)  
#list to dict comprehension
new_dict={key:value for key ,value in zip(list_one,list_two)}
print(new_dict)
#print(zip.__doc__)
l4=[[list_one[i],list_two[i]] for i in range(len(list_one))]
print(l4)

#dictionary by two list
d3={list_one[i]:list_two[i] for i in range(len(list_one))} #for lw in list_two}
print(d3)

