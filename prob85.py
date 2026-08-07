# Problem 85 - Power Function


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print(base, "to the power", exponent, "is:", power(base, exponent))
