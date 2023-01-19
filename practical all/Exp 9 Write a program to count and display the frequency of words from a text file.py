#Write a program to count and display the frequency of words from a text file "test.txt"
with open("test.txt",'r') as F:
    w=F.read().split()
    for j in set(w):
        print(j,":",w.count(j))