income = float(input("Enter your income: "))
if income <= 1000:
    print("Your amount of taxes owed is: ", round((income * 0.05), 2))
elif 2000 >= income > 1000:
    print("Your amount of taxes owed is: ", round((income * 0.10), 2))
else:
     print("Your amount of taxes owed is: ", round((income * 0.15), 2))