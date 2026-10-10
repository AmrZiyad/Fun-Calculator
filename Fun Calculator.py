# Part 1: Write four functions with def. Use return to send answers back.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Part 4: Put Parts 2 and 3 inside a try block
try:
    # Part 2: Ask for two numbers with input() and float(). Then ask for the operation.
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation (add, subtract, multiply, divide): ").strip().lower()

    # Part 3: Use if and elif to compare the operation with each word.
    if operation == "add":
        result = add(num1, num2)
        print(f"Result: {result}")
    elif operation == "subtract":
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif operation == "divide":
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Incorrect operation.")

# Part 4: Handle exceptions and add a finally block
except ValueError:
    print("Error: Please enter numbers only, letters are not allowed.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Thank you for using the calculator!")
