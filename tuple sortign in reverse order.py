# reversing the list of tuples
di={"a":10,"b":100,"c":1} # di is declered as dictionary
print("The sorted dictionary on basis on alphabite in reverse order : ",sorted(di,reverse=True))
print("The sorted dictionary on basis on alphabite  : ",sorted(di))
temp=list()# is temp veriable of type list
for k,v in di.items():# k,v loopes through the value of key pair respectively
    k,v=v,k # swapping the value of key and value in order to make first element as numbers
    temp=temp+[(k,v)]  # concating the empty list with swapped list of tuples
print("The soretd list of tuples on basis of number in reverse order:",sorted(temp,reverse=True))  # sorting the list of tuples on basis of number in reverse order
print("The soretd list of tuples on basis of number :",sorted(temp)  )# sorting the list of tuples on basis of number
