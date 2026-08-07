# Problem 55 - Check Pangram

string = input("Enter a string: ")

string = string.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for letter in alphabet:
    if letter not in string:
        is_pangram = False
        break

if is_pangram:
    print("Pangram")
else:
    print("Not a Pangram")
