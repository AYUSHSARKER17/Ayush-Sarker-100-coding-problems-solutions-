# Problem 90 - Magic Number


def is_magic(n):
    while n > 9:
        sum_digits = 0
        while n > 0:
            sum_digits = sum_digits + (n % 10)
            n = n // 10
        n = sum_digits
    return n == 1


num = int(input("Enter a number: "))

if is_magic(num):
    print(num, "is a Magic Number")
else:
    print(num, "is not a Magic Number")
