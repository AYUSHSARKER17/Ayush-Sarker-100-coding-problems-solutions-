# Problem 3 - Swap two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swap: num1 =", num1, ", num2 =", num2)

temp = num1
num1 = num2
num2 = temp

print("After swap: num1 =", num1, ", num2 =", num2)
