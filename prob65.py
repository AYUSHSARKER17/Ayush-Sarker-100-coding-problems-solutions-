# Problem 65 - Linear Search

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
target = int(input("Enter number to search: "))

index = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
