# Problem 20 - Reverse Number

num = int(input("Enter a number: "))

reversed_num = 0
original_num = num

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print("Reversed number:", reversed_num)
