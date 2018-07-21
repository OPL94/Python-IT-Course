import os

folder = os.getcwd()
print(folder)

if not os.path.isdir("myfolder"):
    os.mkdir("myfolder")
os.chdir("myfolder")

file1 = open("newfile.txt", "w+")
file1.write("File in the folder")
file1.seek(0)

line = file1.read()

print(line)
file1.close()
os.chdir(folder)