import customhandling.py
age=int(input("enter your age:"))
if age<18:
    raise TooyoungException("young")
elif age>18 and age<=60:
    raise TooOldException("old")
else:
    print("mail")
