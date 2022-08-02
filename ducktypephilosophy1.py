class Duck:
    def talk(self):
        print("quack quack")
class Dog:
    def talk(self):
        print("bow bow")
class Cat:
    def talk(self):
        print("meow meow")
class Man:
    def leg(self):
        print("2 legs")        
def obj_fun(obj):
    obj.talk()
d=Duck()
obj_fun(d)
dg=Dog()
obj_fun(dg)
c=Cat()
obj_fun(c)
print(hasattr("hello","split"))
m=Man()
obj_fun(m)
        
