from datetime import datetime
print(datetime.now())
start=datetime.now()
print(type(start))
a=0
for i in range(10000):
    a+=(i**100)
end=datetime.now()
print("total time:",str(end-start)[6:])
print("total time:",end-start)
