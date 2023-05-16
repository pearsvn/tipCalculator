print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
split_bill = bill_with_tip/people
final_amount = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_amount}")