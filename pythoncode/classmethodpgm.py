class Student:
    school_name="sv"
    def __init__(self):
        self.city="beng"
        print("school_name is :",self.school_name)
    @classmethod #if i dont decorate it with class method python will not cosidered as class method
    def student_data(cls,name):#cls representing current class
        print("school name is:",cls.school_name)
        print("name of student is:",name)
        #print("city is:",self.city)cannot access instance level attribute in class level method
Student.student_data("me")        
s=Student()
s.student_data("mi")
