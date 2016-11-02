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

sql="select * from user"
cursor.execute(sql)

print cursor.rowcount

rs=cursor.fetchone()
print rs

rs=cursor.fetchmany(3)
print rs


rs=cursor.fetchall()
for row in rs:
    print "userid=%s,username=%s" % row

cursor.close()
conn.close()