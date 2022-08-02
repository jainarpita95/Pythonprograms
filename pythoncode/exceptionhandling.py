try:
    div= 27/0
    print(div)
#except:
   # print("division by zero")
except ZeroDivisionError:
    print("division by zero")#multiple except error we can use
finally:
    print("show")
