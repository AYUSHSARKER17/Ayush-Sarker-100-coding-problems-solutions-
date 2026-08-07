# Problem 60 - Sum of List

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

sum_total = 0
for num in numbers:
    sum_total = sum_total + num

print("Sum:", sum_total)
