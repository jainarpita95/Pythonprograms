class Duck:
    def talk(self):
        print("quack quack")
class Dog:
    def talk(self):
        print("bow bow")
class Cat:
    def talk(self):
        print("meow meow")
class Person:
    def walk(self):
        print("walk through leg")
for obk in Duck(),Dog(),Cat(),Person():
    obk.talk()
    print(type(obk))
"""def obj_fun(obj):
    obj.talk()
    
d=Duck()
obj_fun(d)
dg=Dog()
obj_fun(dg)
c=Cat()
obj_fun(c)"""
         
