string = input("Enter a string: ")

lowercase_letters = ""

for char in string:
    if char.islower():
        lowercase_letters += char

print(lowercase_letters)
