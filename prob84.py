# Problem 84 - Sum of Numbers


def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)


num = int(input("Enter a number: "))
print("Sum from 1 to", num, "is:", sum_numbers(num))
