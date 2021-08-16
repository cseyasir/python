directory = dict()
for i in range(3):

 def add():
    print("enter the detals to add to directory")
    first = input("enter the full name ")
    last = input("enter the last name")
    number = int(input("enter the number"))
    directory[first,last]=number

 def search():
    firs=input("enter the first name of person ")
    las = input("enter the last name")
    for first,last in directory:
      if (first,last) == (firs,las):
        print("The number of ",firs,las,"is",directory[first, last])
      else:
        print("data not found")

 value=input("press 1 to add\n press 2 to search")
 if value=="1":
    add()
 elif value=="2":
    search()
 print(directory)
