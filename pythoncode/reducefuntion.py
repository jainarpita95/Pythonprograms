from functools import reduce
num_list=list(range(0,11))
total=reduce(lambda x,y:x+y,num_list)
print(total)
#nem add function
def add_num(a,b):
  print(f"sum is {a+b}")
#print(add_num(3,4))  
