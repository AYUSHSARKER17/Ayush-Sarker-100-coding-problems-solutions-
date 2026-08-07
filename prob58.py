# Problem 58 - Second Largest

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element:", second_largest)
