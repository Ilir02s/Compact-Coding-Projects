import random

print("\n--Welcome to the Heads or Tails Random Generator --\n")

choice_heads_tails = int(input("Please chooose '1' or '2': "))

random_number = random.randint(0, 1)

if random_number == 1 or 0:
    print("Heads")
else:
    print("Tails")