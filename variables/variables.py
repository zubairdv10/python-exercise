for varl in range (21,2,-2):
    print(varl)
#this is a countdown loop starting at 2 to 2 subtracting 2
else:
    print ("enough with loops")

cars=["VW","BMW","Ford","Mazda","Tata"]
for myCars in cars:

    if myCars=="Ford":
        continue
    print(myCars)
    for class2 in "Life choices":
        print (class2)


bikes=["Suzuki","Kawasaki","Honda","Ducatti","Vuka"]
for myCars1 in cars:
    for myBikes in bikes:
        print(myCars,myBikes)