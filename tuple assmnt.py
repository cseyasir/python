#tuple assmnt is as below:
hand=open("text.txt")#opening of file
for line in hand:#looping through the lines in the file
    line=line.split()# spliting the lines into elements of list
    name,domin=line[1].split("@")
    print("user name is:",name)
    print("the domain is:",domin)
    day=line[2]
    print("the date is :",day)
z="1,2"
a,b=z.split(",")
print(a,b)