class A:
    @staticmethod
    def m1():
        print("A static")
class B(A):
    @staticmethod
    def m2():
        super(B,B).m1()
        print(id(B))
B.m2()    
