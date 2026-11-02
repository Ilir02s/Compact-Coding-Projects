# BMI calculator

height = input("Please insert your height in m: ")
weight = input("Please insert your weight in kg: ")

bmi = int(weight) / float(height) ** 2
print(int(bmi))