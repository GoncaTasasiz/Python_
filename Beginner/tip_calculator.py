print("Welcome to tip calculator!")
bill = float(input ("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = bill + bill * tip / 100
#print(bill_with_tip)
bill_per_person = (bill_with_tip / people)
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
 
