print("Hello. Welcome to the password strength checker.")
password = input("What's your password? ")
score = 0

if len(password) >= 8:
    score += 2

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True

if has_upper: score +=2

has_lower = False
for char in password:
    if char.islower():
        has_lower = True

if has_lower: score +=2

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True

if has_digit: score +=2

has_symbol = False
for char in password:
    if not char.isalnum():
        has_symbol = True

if has_symbol: score += 2

if score >= 9:
    print("Fort Knox! Your password is strong.")
elif score >= 6 and score <= 8:
    print("Decent, but could use a little more armor.")
else:
    print("Yikes. Your password is easy to crack.")

print(f"Your score is {score}/10.")