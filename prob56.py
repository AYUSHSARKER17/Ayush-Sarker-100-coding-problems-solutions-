# Problem 56 - Caesar Cipher (Basic)

text = input("Enter text: ")
shift = int(input("Enter shift value: "))

result = ""
for char in text:
    if char.isalpha():
        if char.isupper():
            result = result + chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            result = result + chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    else:
        result = result + char

print("Encrypted:", result)
