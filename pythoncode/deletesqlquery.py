import pymysql
try:
     con=pymysql.connect(host="localhost",database="demo_db",user="root",password="arpita123")
     cursor=con.cursor()
     cursor.execute("delete from employees where eno=100")
     print("data deleted")
     print()
     con.commit()
     cursor.execute("select * from employees")
     data=cursor.fetchone()
     print(data)
    

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()    
