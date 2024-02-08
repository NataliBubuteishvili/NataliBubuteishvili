numbers = []
operations = []

while True:
    number = input("Enter a number: ")
    operation = input("Enter an operation: ")
    numbers.append(int(number))
    operations.append(operation)
    if operation == "=":
        break


result = numbers[0]

for i in range(len(numbers)-1):
    if operations[i] == "+":
        result += numbers[i + 1]
    elif operations[i] == "-":
        result -= numbers[i + 1]
    elif operations[i] == "*":
        result *= numbers[i + 1]
    elif operations[i] == "/":
        result /= numbers[i + 1]
    else:
        print("Invalid operation")

print(int(result))
