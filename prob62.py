# Problem 62 - Remove Duplicate

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)
