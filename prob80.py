# Problem 80 - Currency Converter


def convert_currency(amount, rate):
    return amount * rate


amount = float(input("Enter amount: "))
rate = float(input("Enter conversion rate: "))

converted = convert_currency(amount, rate)
print("Converted amount:", converted)
