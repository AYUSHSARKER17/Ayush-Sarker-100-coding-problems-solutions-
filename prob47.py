# Problem 47 - Count Consonants

string = input("Enter a string: ")

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0

for char in string:
    if char in consonants:
        count = count + 1

print("Number of consonants:", count)
