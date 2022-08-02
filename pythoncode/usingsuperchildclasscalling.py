class P:
    def __init__(self):
        print("p init")
    def m1(self):
        print("p m1")
    @classmethod
    def m2(cls):
        print("p class")
    @staticmethod
    def m3():
        print("p static")
class C(P):
    @classmethod
    def m1(cls):
        #super().__init__() invalid
        #super().m1() invalid
        #P.m1(self)will not work
        super().m2()
        super().m3()

C.m1()
#c=C()
#c.m1()
        
