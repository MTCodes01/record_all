#Write a program in python to find the fibonacci series

def fibonacci(x):
    a,b=0,1
    count=0
    while count<x:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
while True:
    print(" ")
    n=int(input("How many terms:"))
    fibonacci(n)