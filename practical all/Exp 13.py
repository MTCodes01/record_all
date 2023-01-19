#To add,delete and display the record using list through stack
employee=[]
c="y"
while c=="y":
    print("1)PUSH")
    print("2)POP")
    print("3)Display")
    ch=int(input("Enter your choice:"))
    if ch==1:
        eID=input("Enter employee number:")
        ename=input("Enter employee name:")
        employee.append((eID,ename))
    elif ch==2:
        if employee==[]:
            print("Stack is empty!")
        else:
            eID,ename=employee.pop()
            print("Deleted element is:",eID,ename)
    elif ch==3:
        for i in range(len(employee)-1,-1,-1):
            print(employee[i])
    else:
        print("Wrong input!")
    c=input("Do you want to continue or not?(y/n):")