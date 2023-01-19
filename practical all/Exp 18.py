#Connectivity program number:2
#Read records from student table and display it,Search particular student details based on their marks.
import mysql.connector as my
x=my.connect(host='localhost',user='root',password='password',database='data')
if x.is_connected():
    print("Connected Successfully!")
c=x.cursor()
c.execute("SELECT * FROM Students;")
r=c.fetchall()
print("\nRecords are:")
for i in r:
    print(i)
m=int(input("\nEnter marks for searching:"))
c.execute("SELECT * FROM Students WHERE mark>{};".format(m))
r=c.fetchall()
for i in r:
    print(i)
x.close()