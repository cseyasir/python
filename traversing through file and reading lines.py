handle=open("jai.py")
count=0
big_number=0
for line in handle:
    lines=line.rsplit()
    for words in lines:
     length=len(words)
     if length>big_number:
         big_number=length
         word1=words
if big_number>length:
         print(word1,big_number)




