# Problem 63 - Find Maximum Frequency

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]

max_count = 0
max_num = numbers[0]

for num in numbers:
    count = 0
    for n in numbers:
        if num == n:
            count = count + 1
    if count > max_count:
        max_count = count
        max_num = num

print("Most frequent element:", max_num, "with frequency", max_count)
