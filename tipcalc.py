print("Welcome to Tip Calculator!")
bill=float(input("What is you Total Bill?  \n"))
tip= float(input("How much tip would like to give? 10, 12 15 or 20: "))
person =float(input("How many people to split the bill? : "))
amount =(bill+(bill*(tip/100)))/person
print(f"Each person should pay: {round(amount,2)}")