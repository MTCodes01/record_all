#Write a program to copy the content of a text file "Orginal.txt" to "Copy.txt"
with open("Orginal.txt",'r') as f1,open("Copy.txt",'w') as f2:
    c=f1.readlines()
    for line in c:
        f2.write(line)
        f2.flush()
    print("Successfully Copied to another file...")