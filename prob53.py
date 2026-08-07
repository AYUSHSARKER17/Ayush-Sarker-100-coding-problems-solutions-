# Problem 53 - Remove Spaces

string = input("Enter a string: ")

result = ""
for char in string:
    if char != " ":
        result = result + char

print("Result:", result)
