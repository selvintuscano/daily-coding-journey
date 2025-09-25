def convert_case(text):
    upper = text.upper()   # Converts to UPPERCASE
    lower = text.lower()   # Converts to lowercase
    return upper, lower


n = "Hello World"
upper_text, lower_text = convert_case(n)

print("Original String:", n)
print("Uppercase:", upper_text)
print("Lowercase:", lower_text)
