__author__ = 'asus'
import MySQLdb


conn=MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='zp',
    passwd='a',
    charset='utf8'

)
cursor=conn.cursor()

print conn
print cursor

cursor.close()
conn.close()