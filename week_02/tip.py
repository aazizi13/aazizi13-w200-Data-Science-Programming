price = float(input ("Enter the price of a meal: "))

tip = float(price) * 0.16
tip = round(tip, 2)
total = price + tip
total = round(total, 2)

print("A 16% tip would be:", tip)
print("The total including tip would be:", total)