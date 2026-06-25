print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))
tip_percentage = (tip / 100) * bill
final_bill = bill + tip_percentage
people_final = final_bill / people
print(f"The final amount to be paied by each person is {people_final}")

