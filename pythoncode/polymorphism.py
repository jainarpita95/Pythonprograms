class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(50)
b2=Book(60)
add_book=b1+b2
print(add_book)
        
