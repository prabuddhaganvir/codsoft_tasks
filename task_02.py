
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# Get user input
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
    exit()

operation = input("Choose operation (+, -, *, /): ")

# Perform calculation based on user choice
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Error: Invalid operation. Please choose +, -, *, or /.")
    exit()

# Display the result
print(f"Result: {result}")
