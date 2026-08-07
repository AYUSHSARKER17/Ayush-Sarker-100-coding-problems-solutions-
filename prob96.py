# Problem 96 - Decimal to Octal

num = int(input("Enter a number: "))

octal = ""
if num == 0:
    octal = "0"
else:
    while num > 0:
        octal = str(num % 8) + octal
        num = num // 8

print("Octal:", octal)
