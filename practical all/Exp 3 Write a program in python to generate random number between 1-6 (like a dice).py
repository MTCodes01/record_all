#Write a program in python to generate random number between 1-6 (like a dice)
import random
while True:
    x=random.randint(1,6)
    try:
        print(x,"\n"*3)
    except KeyboardInterrupt:
        print("\nyour number is",x)
        if input("Do you want to play more?")!='y':
            break