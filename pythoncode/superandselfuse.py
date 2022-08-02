class P:
    a=10
    def __init__(self):
        self.b=20
class C(P):
    def m1(self):
        print(super().a)
        print(self.b)
        print(self.a)
        #print(super().b)this is invalid.
c=C()
c.m1()
