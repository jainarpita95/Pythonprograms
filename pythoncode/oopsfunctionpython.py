class Student:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def disp_data(self):
        print(f"student name {self.name} and city is {self.city}")
name=input("enter your name")
city=input("enter your city")
s_one=Student(name,city)
s_one.disp_data()
