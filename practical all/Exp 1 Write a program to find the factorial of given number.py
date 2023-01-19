#Write a program to find the factorial of given number

def facto(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
while True:
    n=int(input("Enter the number:"))
    print(facto(n))
    print(" ")