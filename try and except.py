for i in range(2):
 num1=input("enter the  first number")
 num2=input("enter the  second  number")
 try:
    product=float(num1)*float(num2)
    print("the product of number is:",product)
 except:
    print('"please enter the numeric value"')