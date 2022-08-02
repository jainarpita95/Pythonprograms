class P:
    def m1(self):
        print("first method")
class C(P):
    def m2(self):
        print("child method")
cs=C()
cs.m1()
cs.m2()
