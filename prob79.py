# Problem 79 - BMI Calculator


def calculate_bmi(weight, height):
    return weight / (height**2)


weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
