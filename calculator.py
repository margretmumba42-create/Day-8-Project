# calculator.py

def calculator():
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask user for an operator
    operator = input("Enter the operator (+, -, *, /, %, **): ")

    # Calculate and print the result
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif operator == "**":
        result = num1 ** num2
    else:
        print("Error: Invalid operator.")
        return

    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
