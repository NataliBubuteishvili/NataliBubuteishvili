def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None

result = 0
continue_calculation = True

while continue_calculation:
    num1 = float(input("Enter a number: "))
    operation1 = input("Enter an operation: ")
    num2 = float(input("Enter a number: "))
    operation2 = input("Enter an operation: ")

    if operation1 == "=":
        break
    if operation2 == "=":
        break
    else:
        result = calculate(num1, num2, operation1)

print(result)