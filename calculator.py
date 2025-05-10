# ADITYANAHA_CodSoft_Simple Calculator

def calculator():
    print("Calculator ON!")
    
    # Getting input numbers from user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation symbol (+, -, *, /): ")

    # Performing calculation
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

calculator()