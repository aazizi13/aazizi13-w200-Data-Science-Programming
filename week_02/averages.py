a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

arimean = float((a + b)/2)
geomean = float(((a * b) ** (1/2)))
rootmean = float((((a ** 2) + (b ** 2))/2) ** (1/2))

x = float(input("Enter 1 to get Arithemic mean, 2 to get Geometric mean, 3 to get root-mean square")) 
if x == 1:
    print ("The arithmertric mean is ", arimean)
elif x == 2:
    print ("The geometric mean is ", geomean)
elif x == 3:
    print ("The root-mean-square mean is ", rootmean)
else:
    print("")
    