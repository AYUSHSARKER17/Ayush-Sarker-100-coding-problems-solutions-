# Problem 61 - Average

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

sum_total = 0
for num in numbers:
    sum_total = sum_total + num

average = sum_total / len(numbers)
print("Average:", average)
