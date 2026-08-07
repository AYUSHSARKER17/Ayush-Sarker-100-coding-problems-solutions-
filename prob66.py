# Problem 66 - Bubble Sort

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted array:", numbers)
