# Problem 59 - Smallest

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)
