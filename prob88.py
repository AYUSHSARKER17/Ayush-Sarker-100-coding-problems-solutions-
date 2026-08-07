# Problem 88 - Happy Number


def is_happy(n):
    seen = []
    while n != 1 and n not in seen:
        seen.append(n)
        sum_sq = 0
        while n > 0:
            digit = n % 10
            sum_sq = sum_sq + (digit * digit)
            n = n // 10
        n = sum_sq
    return n == 1


num = int(input("Enter a number: "))

if is_happy(num):
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")
