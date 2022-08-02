class Student:
    school_name="sv"
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def disp_data(self):
        print(f"student name {self.name} and city is {self.city}")
        print("school name is",self.school_name)
name=input("enter your name")
city=input("enter your city")
s_one=Student(name,city)
s_one.disp_data()
print(s_one.school_name)
print(s_one.name)
print(s_one.__dict__)#__dict__ to give all description in form of dictionary about object
print(Student.__dict__)
