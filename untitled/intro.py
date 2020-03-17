print("testing..")
a = 4
b = 7
c_squared = a**2 + b**2

c = c_squared **(1/2)
print (c)

import math

# new method
c = math.sqrt(c_squared)
print(c)
print(math.sqrt(c_squared))

number = input("give me your number ?")
print("your number is, 27384957", number)

# Given a number, create a program which checks
# if a number is even or odd. If the number
# is even print "Even" else print "Odd".
# If the number is both divisible by 2 and
# 3 print "EvenOdd"

# Input: Type a number here: 4 ii
# Output: even

# Input: type a number here : 6
# Output: EvenOdd
number = int(input("type a number here: "))
if number % 2 == 0:
    print ("Even")
if number % 3 == 0:
    print("Odd")