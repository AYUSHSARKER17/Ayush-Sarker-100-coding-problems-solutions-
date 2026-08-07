# Problem 19 - Count Digits

num = input("Enter a number: ")

count = 0
for digit in num:
    if digit.isdigit():
        count = count + 1

print("Number of digits:", count)
