class A:
    def m1(self,name):
        self.name=name
        print("class A")
        print(id(self))
       # print(self.__dict__)
class B(A):
    def m1(self,name):
        super().m1(name)
        print("class B")
class C(B):
    def m1(self,name):
        super().m1(name)
        print("class C")
class D(C):
    def m1(self,name):
        super().m1(name)
        print("class D")
class E(D):
    def m1(self,name):
        A.m1(self,name)
        #super(A,self,name).m1()
        print(id(self))
       # print(self.__dict__)
e=E()
e.m1("na")
print(id(e))
