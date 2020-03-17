strSpeed=int(input("Please enter your average speed\n"))
strRSpeed=int(input("Please enter road speed\n"))

if (strSpeed<60):
    print("Ok")
elif (strSpeed>strRSpeed):
    demerit=(strSpeed-strRSpeed)//5
    print(demerit, "points")
if (demerit > 12):
            print("Its time to go to jail")
elif(demerit < 12):
            print("You're free for now")
