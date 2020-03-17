a=33
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
x=0
y=5
strFname=input("Please enter first name\n")
strSname=input("Please enter surname\n")
strExmark=int(input("Please enter exam mark\n"))
if (strExmark>79) and (strExmark<101):
   print("first name", strFname, "surname",strSname, "Grade A-Outstanding")
if (strExmark>60) and (strExmark<79):
    print("first name", strFname, "surname", strSname, "Grade B-Satisfactory")
if (strExmark>50) and (strExmark<59):
    print("first name", strFname, "surname", strSname, "Grade C-Average")
if (strExmark>0) and (strExmark<49):
    print("first name", strFname, "surname", strSname, "Grade D-Fail")