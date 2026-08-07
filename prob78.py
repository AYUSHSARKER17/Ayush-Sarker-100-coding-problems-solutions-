# Problem 78 - Temperature Converter


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


choice = input("Convert 1: Celsius to Fahrenheit, 2: Fahrenheit to Celsius: ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))
else:
    print("Invalid choice")
