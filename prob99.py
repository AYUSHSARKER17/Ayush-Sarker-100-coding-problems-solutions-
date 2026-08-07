# Problem 99 - Binary Palindrome

num = int(input("Enter a number: "))

binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

reversed_binary = ""
for i in range(len(binary) - 1, -1, -1):
    reversed_binary = reversed_binary + binary[i]

if binary == reversed_binary:
    print("Binary palindrome")
else:
    print("Not a binary palindrome")
