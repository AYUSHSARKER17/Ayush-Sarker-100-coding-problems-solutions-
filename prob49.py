# Problem 49 - Count Characters

string = input("Enter a string: ")

count = 0
for char in string:
    if char != " ":
        count = count + 1

print("Number of characters:", count)
