#Write a program to remove all the lines that contains the letter 'a' from a text file "Sample.txt"
"""import os
f1=open("sample.txt",'r')
f2=open("content.txt",'w')
f3=open("temp.txt",'w')
content=f1.readlines()
for line in content:
    if 'a' in line:
        print(line)
        f2.write(line)
        f2.flush()
    else:
        f3.write(line)
        f3.flush()
f1.close()
f2.close()
f3.close()
os.remove("sample.txt")
os.rename("temp.txt","sample.txt")"""
import os
with open("sample.txt",'r') as f1,open("temp.txt",'w') as f2:
    for line in f1.readlines():
        if 'a' not in line:
            f2.write(line)
            f2.flush()
os.remove("sample.txt")
os.rename("temp.txt","sample.txt")
print(list(range(int('100',2))))