# Problem 64 - Search Element

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
target = int(input("Enter number to search: "))

found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
