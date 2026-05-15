first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = first + second
    
elif operation == '-':
    result = first - second

elif operation == '*':
    result = first * second

elif operation == '/':
    if second != 0:
        result = first / second
    else:
        result = "Error: Division by zero is not allowed."

else:
    result = "Invalid operation. Please enter one of +, -, *, /."

print(f"The result is: {result}")