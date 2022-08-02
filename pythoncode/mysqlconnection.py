from pymysql import * 
try:
    con=connect(host="localhost",user="root",password="arpita123")
    cursor=con.cursor()
    cursor.execute("CREATE DATABASE demo_db6")
    print("Database created successfully")
    con.commit()
except DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
