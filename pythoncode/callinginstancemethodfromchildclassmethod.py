class P:
    def __init__(self):
        print("init")
        print(id(self))
    def m1(self):
        print("m1")
class C(P):
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
        print(id(cls))
C.m2()        
        
        
