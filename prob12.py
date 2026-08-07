# Problem 12 - Sum of 1 to N

n = int(input("Enter a number: "))

sum_total = 0
for i in range(1, n + 1):
    sum_total = sum_total + i

print("Sum of 1 to", n, "is:", sum_total)
