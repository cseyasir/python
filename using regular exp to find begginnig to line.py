import re   #before using regulae expression we must import the libery of it as import re
count=0
fname=open("text.txt")       #opening the file
for lines in fname:          #looping through the lines in file
    line=lines.rstrip()      #removing whitespace and new lines
    if re.search("^From .+@.+mon",line):   # searching the sting using flags as re.search("string",falgs)
        count+=1
        print(line)
print("No Of Lines",count)#printing Number of Lines
