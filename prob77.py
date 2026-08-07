# Problem 77 - LCM Function


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM:", lcm(num1, num2))
