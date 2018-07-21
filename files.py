import os

folder = os.getcwd()
print(folder)

file1=open("data.txt", "w")
file1.write("Hello world my name is Omar\n test\n")
file1.close()

file1=open("data.txt", "r")
content = file1.read()
print(content)

print("*" * 50)

file1.seek(0);count = 0
line = file1.readline()

while  line:
    print(line.strip())
    count += 1
    line = file1.readline()

print("number of line is %d" % (count))

file1.close()

