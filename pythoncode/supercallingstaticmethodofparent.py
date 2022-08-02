class P:
    a=10
    def __init__(self):
        self.b=10
        print(id(self.b))
    def m1(self):
        print("parent instance")
    @classmethod
    def m2(cls):
        print("parent class")
    @staticmethod
    def m3():
        print("parnet static")
class C(P):
    a=888
    def __init__(self):
        self.b=999
        print(self.b)
        super().__init__()
        print(self.a)
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        print(id(self.b))
c=C()        
        
