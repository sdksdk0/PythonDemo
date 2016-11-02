__author__ = 'asus'
import MySQLdb

conn=MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='zp',
    passwd='a',
    db='mysqlforpython',
    charset='utf8'

)
cursor=conn.cursor()

sql_insert="insert into user(userid,username) values(10,'name10')"

sql_update="update user set username='name3'  where userid=1"

sql_delete="delete from user where userid=10"

cursor.execute(sql_insert)
print cursor.rowcount
cursor.execute(sql_update)
print cursor.rowcount
cursor.execute(sql_delete)
print cursor.rowcount

conn.commit()

cursor.close()
conn.close()