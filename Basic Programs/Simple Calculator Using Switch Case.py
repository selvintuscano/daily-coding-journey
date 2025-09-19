# Simple calculator using if-elif-else

a = 20
b = 5
operator = '+'  # change this to -, *, /, %

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b if b != 0 else "Division by zero error"
elif operator == '%':
    result = a % b if b != 0 else "Modulo by zero error"
else:
    result = "Invalid operator"

print(f"{a} {operator} {b} = {result}")
