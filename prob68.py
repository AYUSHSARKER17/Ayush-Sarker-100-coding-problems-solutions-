# Problem 68 - Insertion Sort

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = key

print("Sorted array:", numbers)
