#user define exception
class TooYoungException(Exception):
    def __init__(self,message):
        self.message=message
class TooOldException(Exception):
    def __init__(self,message):
        self.message=message
        
age=int(input("enter your age:"))
if age<18:
    raise TooYoungException("young")
elif age>18 and age<=60:
    raise TooOldException("old")
else:
    print("mail")

