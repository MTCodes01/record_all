#To implement basic operation of a stack
s=[]
c="y"
while c=="y":
    print("1)PUSH")
    print("2)POP")
    print("3)Display")
    ch=int(input("Enter your choice:"))
    if ch==1:
        a=input("Enter any number:")
        s.append(a)
    elif ch==2:
        if s==[]:
            print("Stack is empty!")
        else:
            print("Deleted element is:",s.pop())
    elif ch==3:
        for i in range(len(s)-1,-1,-1):
            print(s[i])
    else:
        print("Wrong input!")
    c=input("Do you want to continue or not?(y/n):")