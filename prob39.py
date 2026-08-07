# Problem 39 - Pascal Triangle

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    coeff = 1
    for k in range(i + 1):
        print(coeff, end=" ")
        coeff = coeff * (i - k) // (k + 1)
    print()
