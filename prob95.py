# Problem 95 - Binary to Decimal

binary = input("Enter a binary number: ")

decimal = 0
power = 0
for i in range(len(binary) - 1, -1, -1):
    decimal = decimal + int(binary[i]) * (2**power)
    power = power + 1

print("Decimal:", decimal)
