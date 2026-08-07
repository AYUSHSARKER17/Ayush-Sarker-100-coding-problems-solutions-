# Problem 92 - Collatz Sequence

num = int(input("Enter a number: "))

sequence = []
while num != 1:
    sequence.append(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1

sequence.append(1)
print("Collatz Sequence:", sequence)
