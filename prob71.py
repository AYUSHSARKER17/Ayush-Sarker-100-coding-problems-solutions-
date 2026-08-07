# Problem 71 - Find Missing Number

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

n = len(numbers) + 1
total_sum = (n * (n + 1)) // 2
current_sum = 0

for num in numbers:
    current_sum = current_sum + num

missing = total_sum - current_sum
print("Missing number:", missing)
