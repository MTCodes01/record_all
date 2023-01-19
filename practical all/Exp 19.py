import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="learner",passwd="fast",database="test")
if mycon.is_connected()==False:
    print("Error connecting to MySQL database!")
cursor=mycon.cursor()
cursor.execute("SELECT * FROM student")
data=cursor.fetchmany(3)
count=cursor.rowcount
for row in data:
    print(row)
mycon.close()