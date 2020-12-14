#*****SOIL NUTRIENT VALUE DETECTION AND DISPENSER SYSTEM ******
print("*****SOIL NUTRIENT VALUE DETECTION AND DISPENSER SYSTEM ******")
nit_color_1=int(input("enter the value of ist nitrogen color sensor"))  # reading the 1st nitrogen color sensor

nit_color_2=int(input("enter the value of 2nd nitrogen color sensor"))  # reading the 2st nitrogen color sensor

nit_color_3=int(input("enter the value of 3rd nitrogen color sensor ")) # reading the 3rd nitrogen color sensor

cal_color_1=int(input("enter the value of 1st cal color sensor "))      # reading the 1st calcium color sensor

cal_color_2=int(input("enter the value of 2nd cal color sensor "))      # reading the 2nd calcium color sensor

cal_color_3=int(input("enter the value of 3rd cal color sensor "))      # reading the 3rd calcium color sensor

mag_color_1=int(input("enter the value of 1st mag color sensor "))     # reading the 1st magnesium color sensor

mag_color_2=int(input("enter the value of 2nd mag color sensor "))     # reading the 2nd magnesium color sensor

mag_color_3=int(input("enter the value of 3rd mag color sensor "))     # reading the 3rd magnesium color sensor

nit=50          # nitrogen threshold

cal=50          # calcium threshold

mag=50           # magnesium threshold

nit_mean=(nit_color_1+nit_color_2+nit_color_3)/3   # nitrogen mean

cal_mean=(cal_color_1+cal_color_2+cal_color_3)/3    # calcium mean

mag_mean=(mag_color_1+mag_color_2+mag_color_3)/3     # magnesium mean

if nit_mean<nit:     # comparing the mean value of nitrogen
    print("nitrogen value is less than thrshd")
    print("nitrogen motor on")    # making motor onn

else: # value greater than threshold
    print("nitrogen value is greater than thrshd")
    print("nitrogen motor off") # making motor off

if cal_mean < cal:    # comparing the mean value of calcium
    print("calcium value is less than thrshd")
    print("calcium motor on")  # making motor onn

else:  # value greater than threshold
    print("calcium value is greater than thrshd")
    print("calcium motor off") # making motor off

if mag_mean < mag:     # comparing the mean value of magnesium
    print("magnesium value is less than thrshd")
    print("magnesium motor on") # making motor onn

else:  # value greater than threshold
    print("magnesium value is greater than thrshd")
    print("magnesium motor off") # making motor off
