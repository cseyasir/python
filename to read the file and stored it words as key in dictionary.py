file=open('tex.txt')


name=dict()
for line in file:
    print(line)
    name[line]="y"
print(name)
check='y' in name
print(check)
