================================================================
#table creation
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='employees')
cur = conn.cursor()
#cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print('=========================WELCOME TO START EMPLOYEE MANAGEMENT SYSTEM============================================================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()



n=int(input('enter your choice='))
print()

if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT  INTO log_id (user_id,password) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import mainp

if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from log_id where password='"+str (passwd)+"' and user_id=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchall() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import mainp

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MAINP.PY FILE #
import time
print ("\t\t\t",time.ctime())

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
mycursor=conn.cursor()


def menu():
    print("          EMPLOYEES MANAGEMENT SYSTEM            ")
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
        print("1.login")
        print("2.employee registeration")
        print("3.employee details")
        print("4.update salary")
        print("5.employees list")
        print("6.know the number of employees")
        print("7.work experience")
        print("8.know your salary")
        print("exiting")
        choice=int(input("      enter the choice:          "))
        if choice==1:
            login()
        elif choice==2:
            register()
        elif choice==3:
            details()
        elif choice==4:
            em_salary()
        elif choice==5:
            em_list()
        elif choice==6:
            em_count()

        elif choice==7:
            em_perform()
        elif choice==8:
            salary()
        else:
            print ("exit")
            break
    else : print("Thank You")
def login():
    import sys
    user_id=input("enter USER ID :")
    pwd=int(input("enter the password :"))
    if user_id == 'vishal'and pwd == 6054:
        print("welcome to EMPLOYEE MANAGEMENT SYSTEM ")
    else:

        print("invalid user id and password")
        sys.exit()


def register():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
    mycursor=conn.cursor()
    v_em_no=int(input("enter your employee ID"))
    v_em_name=input ("enter your name:")
    v_em_dept=input( "enter department you want to join : ")
    v_em_salary=input ("enter your salary:")
    v_em_age=int(input("enter your age:"))
    v_sql_insert="insert into office values("+int(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"',"+str(v_em_salary)+","+str(v_em_age)+")"
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("congrats you have joined suuceessfully")
    print("       registerd suyccessfully          ")
def details():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
    mycursor=conn.cursor()
    mycursor.execute("select* from OFFICE")
    results=mycursor.fetchall()
    conn.commit()
    for x in results:
        print(x)
def em_salary():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
    mycursor=conn.cursor()
    nam=input("enter your name")
    mycursor.execute("update office set em_salary=em_salary+em_salary*10/100 where em_name='{}'".format(nam))

    conn.commit()


def em_list():
    import mysql.connector as sql
    try:
        conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
        mycursor=conn.cursor()
        mycursor.execute("select em_name from office order by em_name asc")
        list_=mycursor.fetchall()
        for x in list_:
            print (x)
        a=mycursor.rowcount()
        print("total employees are",a)
    except:
        print ("unable to show the list")
def em_count():
    import mysql.connector as sql
    conn=sql.connect(host='localhost',user='root',password='manager',database='employees')
    mycursor=conn.cursor()
    mycursor.execute("select count(distinct em_name) from office")
    count=mycursor.fetchall()
    for x in count:
        print("    numbr of employees:",x)
    conn.commit()



def salary():
    nam=input("enter your name :")
    a=mycursor.execute("select em_salary from office where em_name='{}'".format(nam))
    mycursor.execute(a)
    salary=mycursor.fetchall()
    for x in salary:
        print(        x,"is your current salary",nam       )
    conn.commit()
def em_perform():
    v_em_no=int(input("enter your employee ID"))
    v_em_name=input ("enter your name:")
    v_em_dept=input( "enter department you want to join : ")
    v_em_performance=input("enter your performance:") 
    v_em_work=input ("enter your experience(YEARS):")
    v_sql_insert="insert into em_performance values("+str(v_em_no)+",'" +v_em_name+"','"+v_em_dept+"','"+v_em_performance+"',"+str(v_em_work)+")"
    print(v_sql_insert)
    mycursor.execute(v_sql_insert)
    conn.commit()
    print("performance added")

menu()  # PYTHON MODULE :Tables_in_mysql

