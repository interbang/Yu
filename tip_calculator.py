#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_calc = (tip_percentage * 0.01) + 1

people = float(input("How many people should split the bill? "))
person_bill = (total_bill / people) * tip_calc

person_bill_round = "{:.2f}".format(person_bill)
print(f"Each person should pay: ${person_bill_round}")

