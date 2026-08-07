# Problem 24 - Palindrome Number

num = int(input("Enter a number: "))

original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original == reversed_num:
    print(original, "is a Palindrome")
else:
    print(original, "is not a Palindrome")
