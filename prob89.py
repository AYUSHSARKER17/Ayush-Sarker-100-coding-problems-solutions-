# Problem 89 - Harshad Number


def is_harshad(n):
    original = n
    sum_digits = 0

    while n > 0:
        sum_digits = sum_digits + (n % 10)
        n = n // 10

    return original % sum_digits == 0


num = int(input("Enter a number: "))

if is_harshad(num):
    print(num, "is a Harshad Number")
else:
    print(num, "is not a Harshad Number")
