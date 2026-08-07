# Problem 25 - Armstrong Number

num = int(input("Enter a number: "))

original = num
sum_powers = 0
num_digits = len(str(num))

while num > 0:
    digit = num % 10
    sum_powers = sum_powers + (digit**num_digits)
    num = num // 10

if original == sum_powers:
    print(original, "is an Armstrong Number")
else:
    print(original, "is not an Armstrong Number")
