def regstn(reg):
    reg=reg+".txt"
    try:
      file=open(reg)
      for lines in file:
        print(lines)
    except:
      print("car not regstd")

plate=input("enter the number plate")
lenght=0
area=""
reg=""
def car(plate):
    length=len(plate)//2
    area=plate[:length]


    print(area)
    if area=="jk03":
        print("car of anantanag area of kashmir divison")
    elif area=="jk01":
        print("vehicle of sriginar area of kashmir divison")
    elif area=="jk22":
        print("vehicle  shopian area of kashmir divison")

    elif area == "jk18":
        print("vehicle of  kulgam area of kashmir divison")
    elif area == "jk13":
        print("vehicle of pulwama of kashmir divison")
    elif area == "jk04":
        print("vehicle of badgam of kashmir divison")
    elif area == "jk05":
        print("vehicle of baramulllah of kashmir divison")
    reg=plate[length:]
    regstn(reg)
car(plate)


