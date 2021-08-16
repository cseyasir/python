print("::::::One Zero Game::::::")
box_1=3
box_2=3
box_3=3
box_4=3
box_5=3
box_6=3
box_7=3
box_8=3
box_9=3
for i in range(9):

 print(" press 1 to select 1 box\npress 2 to select 2 box\npress 3 to select 3 box\npress 4 to select 4 box\npress 5 to select 5 box\npress 6 to select 6 box\npress 7 to select 7 box\npress 8 to select 8 box\npress 9 to select 9 box\n")
 number=int(input("enter your  box number"))
 if number==1 :
    if box_1==0:
         print("0 is already entered")
         continue
    elif box_1==1:
         print("1 is already entered")
         continue
    choice=int(input("enter eiher one or zero in row1 mamd col 1"))
    box_1=choice

 elif number==2:
     if box_2 == 0:
         print("0 is already entered")
         continue
     elif box_2 == 1:
         print("1 is already entered")
         continue
     choice = int(input("enter eiher one or zero in row1 mamd col 2"))
     box_2=choice
 elif number== 3:
     if box_3 == 0:
         print("0 is already entered")
         continue
     elif box_3 == 1:
         print("1 is already entered")
         continue
     choice = int(input("enter eiher one or zero in row1 mamd col 3"))
     box_3=choice
     # selecting row two ones

 elif number==4:
    if box_4==0:
         print("0 is already entered")
         continue
    elif box_4==1:
         print("1 is already entered")
         continue
    choice=int(input("enter eiher one or zero in row2 mamd col 1"))
    box_4=choice
 elif number==5:
    if box_5==0:
         print("0 is already entered")
         continue
    elif box_5==1:
         print("1 is already entered")
         continue
    choice=int(input("enter eiher one or zero in row2 mamd col 2"))
    box_5=choice
 elif number==6:
    if box_6==0:
         print("0 is already entered")
         continue
    elif box_6==1:
         print("1 is    already entered")
         continue
    choice=int(input("enter eiher one or zero in row2 mamd col 3"))
    box_6=choice
    #now row 3
 elif number==7:
     if box_7 == 0:
         print("0 is already entered")
         continue
     elif box_7 == 1:
         print("1 is already entered")
         continue
     choice = int(input("enter eiher one or zero in row3 mamd col 1"))
     box_7=choice
 elif number==8:
     if box_8 == 0:
         print("0 is already entered")
         continue
     elif box_8 == 1:
         print("1 is already entered")
         continue
     choice = int(input("enter eiher one or zero in row3 mamd col 2"))
     box_8=choice
 elif number==9:
     if box_9 == 0:
         print("0 is already entered")
         continue
     elif box_9 == 1:
         print("1 is already entered")
         continue
     choice = int(input("enter eiher one or zero in row3 mamd col 3"))
     box_9=choice

 if (box_1 ==1 and box_2==1 and box_3 ==1):
    print("player1  u won via crossing box 1,2,3 -")
    break
 elif (box_1 ==0 and box_2==0 and box_3 ==0):

    print("player 0 u won via crossing box 1,2,3 -")
    break
 elif (box_4 ==1 and box_5==1 and box_6 ==1):
    print("player 1 so u won via crossing box 4,5,6 --")
    break
 elif (box_4 ==0 and box_5== 0 and box_6 ==0):
    print("player0 u won via crossing box 4,5,6 --" )
    break
 elif (box_7 ==1 and box_8==1 and box_9 ==1):
    print("player 1 so u won via crossing box 7,8,9  ---")
    break
 elif (box_7 ==0 and box_8==0 and box_9 ==0):
    print("player0 u won via crossing box 7,8,9  ---" )
    break
    # now horzontally

 elif (box_1 ==1 and box_4==1 and box_7==1):
    print("player1 u won via crossing box 1,4,7 |")
    break
 elif (box_1 ==0 and box_4==0and box_7 ==0):
    print("player0 u won via crossing box 1,4,7 |")
    break
 elif (box_2 ==1 and box_5==1 and box_8==1):
    print("player1 u won via crossing box 2,5,8 ||")
    break
 elif (box_2 ==0 and box_5== 0and box_8== 0):
    print("player0 u won via crossing box 2,5,8 ||")
    break
 elif (box_3 ==1 and box_6==1 and box_9 == 1):
    print("player1 u won via  crossing box 3,6,9|||")
    break
 elif (box_3 ==0  and box_6==0 and box_9 == 0):
    print("player0 u won via crossing box 3,6,9 ||| ")
    break
 # diganly


 elif (box_3 ==1 and box_5==1 and box_7 == 1):
    print("player1 u won via dignal  crossing box 3,5,7 //")
    break
 elif (box_3 ==0 and box_5==0 and box_7 == 0):
    print("player0 u won via dignal crossing box 3,5,7 //")
    break
 elif (box_1==1 and box_5==1 and box_9 == 1):
    print("player1 u won via dignal  crossing box 1,5,9 \\")
    break
 elif (box_1 ==0 and box_5==0 and box_9 == 0):
    print("player0 u won via dignal  crossing box 1,5,9\\")
    break
 #else:
    #print("No one won")






