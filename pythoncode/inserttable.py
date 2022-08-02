import pymysql
try:
    con=pymysql.connect(host="localhost",database="demo_db",user="root",password="arpita123")
    cursor =con.cursor()
    sql = "insert into employees(eno,ename,esal,eaddr) VALUES(%s,%s,%s,%s)"
    records=[(100,'sachin',1000,'mumbai'),
             (200,'dhoni',2000,'Ranchi'),
             (300,'kholi',3000,'Delhi')]
    cursor.executemany(sql,records)
    print("table inserted sucessfully")
    con.commit()
    print("Records Inserted successfully...")
    
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()    
    
