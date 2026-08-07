# Problem 14 - Sum of Odd Numbers

n = int(input("Enter a number: "))

sum_odd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_odd = sum_odd + i

print("Sum of odd numbers from 1 to", n, "is:", sum_odd)
