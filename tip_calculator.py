#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = float(input("How many people should split the bill?"))
tip_calc = (tip_percentage * 0.01) + 1
person_bill = (total_bill / people) * tip_calc
person_bill_round = round(person_bill, 2)
print(f"Each person should pay {person_bill_round}")
#print(type(total_bill))
