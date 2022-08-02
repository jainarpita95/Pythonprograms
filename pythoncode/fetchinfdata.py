import pymysql
try:
    con=pymysql.connect(host="localhost",database="demo_db",user="root",password="arpita123")
    cursor=con.cursor()
    sql="select * from employees;"
    cursor.execute(sql)
    print("data reterived")
    print()
    data=cursor.fetchall()
    for column in data:
       # print(column) #it is also working
        print("Empolyee Number:",column[0])
        print("Empolyee Name:",column[1])
        print("Empolyee salary:",column[2])
        print("Empolyee Address:",column[3])
        print()
        print()

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()    
    

        
