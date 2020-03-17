Cars=[56,78,34,21,56,34,125,45,89,75,12,56]
#finding the smallest and largest numbers
print("Smallest number is:", min(Cars))
print("Largest number is:", max(Cars))
#finding the total amount
total=sum(Cars)
print("The sum of all the numbers is:", total)
#removing the duplicate numbers
Cars=list(set(Cars))
print("Set after removing duplicate", Cars)