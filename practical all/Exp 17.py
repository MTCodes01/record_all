#Connectivity program number:1
#Write a program to create a database,table and insert values into the table using database connectivity.
import mysql.connector as my
x=my.connect(host='localhost',user='root',password='password',port=3306)
if x.is_connected():
    print("Connected Successfully!")
c=x.cursor()
c.execute("CREATE DATABASE data IF NOT EXISTS")
c.execute("use data")
c.execute("CREATE TABLE detail(roll int PRIMARY key,name char(10),sex char(1),class int,mark int) IF NOT EXISTS")
for i in range(3):
    r=int(input("\nEnter the roll no:"))
    n=input("Enter name:")
    s=input("Enter gender:")
    cl=int(input("Enter your class:"))
    m=int(input("Enter your marks:"))
    R="INSERT INTO detail(roll,name,sex,class,mark) VALUES(%s,%s,%s,%s,%s);"
    val=(r,n,s,cl,m)
    c.execute(R,val)
    x.commit()
x.close()