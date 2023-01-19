#Write a program in python to check if the given number is prime or not
while True:
    num=int(input("Enter a number:"))
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number!")
            break
    else:
        print(num,"is a prime number!")