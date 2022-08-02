class Person:
    city="bang"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print("rollno:",self.rollno)
        print("marks:",self.marks)
        print("city:",super().city)
s1=Student("mary",22,101,90)
s1.display()
