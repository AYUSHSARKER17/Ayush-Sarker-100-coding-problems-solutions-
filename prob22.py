# Problem 22 - Product of Digits

num = int(input("Enter a number: "))

product = 1
temp = abs(num)

while temp > 0:
    digit = temp % 10
    product = product * digit
    temp = temp // 10

print("Product of digits:", product)
