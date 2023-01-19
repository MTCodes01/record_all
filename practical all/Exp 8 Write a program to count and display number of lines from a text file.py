#Write a program to count and display number of lines from a text file "lines.txt"
line=""
count=0
file=open("lines.txt",'r')
i=file.readlines()
for line in i:
    count+=1
print("number of lines in the file is",count)