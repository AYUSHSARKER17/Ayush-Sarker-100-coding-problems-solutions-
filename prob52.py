# Problem 52 - Frequency of Characters

string = input("Enter a string: ")

for char in string:
    count = 0
    for c in string:
        if char == c:
            count = count + 1
    print(char, ":", count)
