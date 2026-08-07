# Problem 73 - Prime Function


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is Prime")
else:
    print(num, "is not Prime")
