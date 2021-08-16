fhandle=open('tex.txt','w')
line="external edited file\n"
fhandle.write(line)
fhandle.close()
fhand=open('tex.txt')
for line in fhand:
    print(line)