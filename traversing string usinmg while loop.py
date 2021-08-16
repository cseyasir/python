string=input("enter the string")
lenght=len(string)
# printing string using while loop
i=0
while(i<lenght):
    one_string=string[i]
    print(one_string)

    i=i+1
# reversing the string
i=1
while(i<=lenght):
    one_string=string[lenght-i]#length-1 so on
    print(one_string)#print last alphabit
    i=i+1