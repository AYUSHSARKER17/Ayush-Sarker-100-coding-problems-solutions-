# Problem 70 - Rotate List

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
k = int(input("Enter rotation count: "))

k = k % len(numbers)
rotated = numbers[-k:] + numbers[:-k]

print("Rotated array:", rotated)
