h=open("newfile.txt","r")
#data=h.read()
#print(data)
#data=h.read(10)
#print(data)
lines=h.readlines()#iterable
for l in lines:
    print(l)
h .close()    
