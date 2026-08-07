# Problem 44 - Reverse String

string = input("Enter a string: ")

reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string = reversed_string + string[i]

print("Reversed string:", reversed_string)
