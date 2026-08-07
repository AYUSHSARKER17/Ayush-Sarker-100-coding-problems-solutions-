# Problem 50 - Uppercase to Lowercase

string = input("Enter a string: ")

result = ""
for char in string:
    if char.isupper():
        result = result + char.lower()
    else:
        result = result + char

print("Result:", result)
