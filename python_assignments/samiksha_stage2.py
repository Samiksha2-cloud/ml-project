# Stage 2: Calculator with Result Check
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = None

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero.")

if result is not None:
    print(f"Result = {result}")
    # Result check logic
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")