from collections import namedtuple
student=namedtuple('student',['name','age','dob'])
s=student('nay','18','251444')
print(s[1])
print(s.name)
p=student('kiy','18','254555')
#for x in p:
   # print(x)
print(getattr(s,'dob'))
li=['manju','19','411167']#intializing list
di={'name':'nikki','age':19,'dob':134578}#intialising dict
print(student._make(li))#both outside and inside student should be same
print(student._make(s))
print(student._make(di))
print(s._asdict())
print(student(**di))
print(s._fields)
print(type(s._fields))
print(s._replace(age='19'))#only temporary changes done
print(s)
