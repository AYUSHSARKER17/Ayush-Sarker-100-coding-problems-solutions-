# Problem 45 - Palindrome String

string = input("Enter a string: ")

string = string.replace(" ", "").lower()
reversed_string = ""

for i in range(len(string) - 1, -1, -1):
    reversed_string = reversed_string + string[i]

if string == reversed_string:
    print("Palindrome")
else:
    print("Not a Palindrome")
