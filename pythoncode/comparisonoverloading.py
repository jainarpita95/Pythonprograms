class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, obj2):
        return self.a < obj2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
         return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a
a = Comparison(1)
b = Comparison(2)
print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)
