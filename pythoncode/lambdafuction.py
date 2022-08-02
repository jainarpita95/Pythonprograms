#lambda function
a=lambda x:x*10
print(a(100))
#map fuction
number_list=list(range(0,5))
l=list(map(lambda x:x*2,number_list))
print(l)
#map function
city="bengluru"
l=list(map(lambda x:x.upper(),city))
print(l)
l="".join(l)#join is function in the list and tuple to join each elementin it .
print(l)
#filter function
num_list=list(range(0,11))
def is_even(num):
    if num%2==0:
        return True
filtered_data=tuple(filter(is_even,num_list))
print(filtered_data)
#map,filter,reduce are higher order function because they take function as argument.
