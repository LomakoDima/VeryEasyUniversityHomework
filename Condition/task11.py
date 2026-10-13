a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = None
        print("Error: division by zero")

if operator in ["+", "-", "*", "/"]:
    if result is not None:
        print("Result:", result)
else:
    print("Invalid operator")
