# Problem 16 - Reverse Multiplication Table

n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(n, "x", i, "=", n * i)
