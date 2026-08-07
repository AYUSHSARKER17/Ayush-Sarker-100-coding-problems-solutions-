# Problem 97 - Decimal to Hexadecimal

num = int(input("Enter a number: "))

hexadecimal = ""
hex_chars = "0123456789ABCDEF"

if num == 0:
    hexadecimal = "0"
else:
    while num > 0:
        hexadecimal = hex_chars[num % 16] + hexadecimal
        num = num // 16

print("Hexadecimal:", hexadecimal)
