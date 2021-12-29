bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
real_tip = (int(tip) / 100) + 1
ammount = (float(bill) / int(people)) * real_tip
print(f"Each person should pay: ${round(ammount,2)}")