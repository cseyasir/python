# tuple operator as list operations like searching element on basis of indexing
tupil="deel"
for i in tupil:# looping through the elements of tuple
  if i==tupil[3]:# if the i == third element print that out
        print("the value of third element is : ",i)
# Slicing the elements in tuple:
print("the seliced protion starting of tuple from 0 element to 2 element",tupil[0:2])
# slicing using file handler
fname=input("enter the name of file")
han=open(fname)
string=""# empty string
for line in han:# looping through the number of lines
    words=line.split()# making list of all lines using split function
    for word in words:# looping through the words in the line
     string=string+word# strong the word in the sting
tu=tuple(string)# making the words as tuple
print(tu)# printing the tuple
length=len(tu)# finding the length of tuple
middle=int(length/2)# median of the tuple
print("The start to middle slice of tuple is:",tu[0:middle])# printing the tuple form start to middle using tuple slicing
print("The  middle to end  slice of tuple is:",tu[middle:])# printing the tuple from middle to end using tuple slicing
