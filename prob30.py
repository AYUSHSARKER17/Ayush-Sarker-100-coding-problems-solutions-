# Problem 30 - Twin Prime Check

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if is_prime(num1) and is_prime(num2) and (num2 - num1 == 2):
    print("Twin Primes")
else:
    print("Not Twin Primes")
