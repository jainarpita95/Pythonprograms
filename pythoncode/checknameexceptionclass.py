class CheckName(Exception):
    def __init__(self,msg):
        self.msg=msg
name=input("enter your name:")        
if "@" in name:
    raise CheckName("name should not have special character")
else:
    print("your name is:",name)
