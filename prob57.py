# Problem 57 - Largest Element

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)
