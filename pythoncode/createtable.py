import pymysql
try:
    con=pymysql.connect(host="localhost",database="demo_db",user="root",password="arpita123")
    cursor =con.cursor()
    sql_query = "create table employees2(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))"
    cursor.execute(sql_query)
    print("table created sucessfully")
    con.commit()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()    
    
