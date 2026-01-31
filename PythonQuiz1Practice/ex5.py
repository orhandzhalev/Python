x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Even numbers in the range: ")

for num in range(x, y + 1):
    if num % 2 == 0:
        print(num)
