# Problem 27 - Strong Number

num = int(input("Enter a number: "))

original = num
sum_factorials = 0
temp = num

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i
    sum_factorials = sum_factorials + factorial
    temp = temp // 10

if original == sum_factorials:
    print(original, "is a Strong Number")
else:
    print(original, "is not a Strong Number")
