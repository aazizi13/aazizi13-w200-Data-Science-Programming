numgas = int(input("Enter the number of gallons: "))
print(numgas, "gallons")

a = numgas * 3.7854 
a = round(a, 4)
print(a, "liters")

b = numgas / 19.5
b = round(b, 3)
print(b, "barrel")

p = numgas * 3.65
p = round(p, 2)
print("The price in US dollars would be", p)
