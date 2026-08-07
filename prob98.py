# Problem 98 - Binary Addition

binary1 = input("Enter first binary number: ")
binary2 = input("Enter second binary number: ")

decimal1 = 0
decimal2 = 0

for i in range(len(binary1) - 1, -1, -1):
    decimal1 = decimal1 + int(binary1[i]) * (2 ** (len(binary1) - 1 - i))

for i in range(len(binary2) - 1, -1, -1):
    decimal2 = decimal2 + int(binary2[i]) * (2 ** (len(binary2) - 1 - i))

result_decimal = decimal1 + decimal2
result_binary = ""

if result_decimal == 0:
    result_binary = "0"
else:
    while result_decimal > 0:
        result_binary = str(result_decimal % 2) + result_binary
        result_decimal = result_decimal // 2

print("Sum in binary:", result_binary)
