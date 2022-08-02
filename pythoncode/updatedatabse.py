import pymysql
try:
     con=pymysql.connect(host="localhost",database="demo_db",user="root",password="arpita123")
     cursor=con.cursor()
     sql_query="update employees set ename ='john' where eno =101"
     cursor.execute(sql_query)
     print("data updated")
     print()
     con.commit()
     sql_query="select * from employees;"
     cursor.execute(sql_query)
     print("data reterived")
     print()
     data=cursor.fetchone()
     for row in data:
         print(row)

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()    
    

        
