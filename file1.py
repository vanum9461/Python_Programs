import os.path
filename="hello1.txt"
if os.path.isfile(filename):
    f=open(filename,"r")
#print(f.readlines())
    for line in f:
        print(line,end="")
else:
    print("File doesn't exit")
