#Write a program to check whether a number is pallindrome or not
n=input("Enter a number:")
if n==n[::-1]:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")