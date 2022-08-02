#write a funtion input as list of number and return a dictionary which will contain
#key as num and value is number of occurence of key i.e.number.
def number_count(num_list):
    dict_count={}
    for i in num_list:
        dict_count[i]=0
        for x,y in dict_count.items():
            x=i
            dict_count[x]=num_list.count(i)
    return dict_count
list_count=number_count([4,4,4,2,2,2,4])
print(list_count)
#method 2
def number_count(num_list):
    dict_count={}
    for i in num_list:
        dict_count[i]=dict_count.get(i,0)+1
    return dict_count
list_count=number_count([1,2,3,1,2,3,4])
print(list_count)
