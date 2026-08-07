# Problem 51 - Lowercase to Uppercase

string = input("Enter a string: ")

result = ""
for char in string:
    if char.islower():
        result = result + char.upper()
    else:
        result = result + char

print("Result:", result)
