# Welcome to the tip calculator.

print("-- Welcome to the tip calculator. --\n")

total_bill = float(input("What was the total bill? $"))

user_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))

people_split = int(input("How many people split the bill? "))

result_1 = round((total_bill / people_split) * 1.10, 2)
result_2 = round((total_bill / people_split) * 1.12, 2)
result_3 = round((total_bill / people_split) * 1.15, 2)

if user_percentage == 10:
    print(f"Each person should pay: ${result_1}")
elif user_percentage == 12:
    print(f"Each person should pay: ${result_2}")
else:
    print(f"Each person should pay: ${result_3}")