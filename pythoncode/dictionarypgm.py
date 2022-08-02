
dict_item={100:2,101:4,103:5}
print(dict_item)
print(dict_item[100])
print(len(dict_item))
print(type(dict_item))
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
x=thisdict.keys()
print(x)
x=thisdict.values()
print(x)
x=thisdict.items()
print(x)
thisdict["year"]="2020"
print(thisdict)
thisdict.update({"year":"2013"})
print(thisdict)
#thisdict["capacity"]="3"
print(thisdict)
thisdict.update({"capacity":"3"})
print(thisdict)
thisdict.pop("capacity")
print(thisdict)
#thisdict.popitem()
#print(thisdict)
del thisdict["year"]
print(thisdict)
#del thisdict
#print(thisdict)
#thisdict.clear()
#print(thisdict)
for x,y in thisdict.items():
   print(x,y)
for x in thisdict:
    print(x)
for x in thisdict:
   print(thisdict[x]) 
print(sum(dict_item.keys()))
print(sum(dict_item.values()))
