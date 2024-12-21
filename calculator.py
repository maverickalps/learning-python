import calculator_art_logo
print(calculator_art_logo.logo[0])
a = int(input("Enter the first number: "))
print("""Pick an operation: 
+
-
*
/
""")
operation = input("Enter the operation: ")
b = int(input("Enter the second number: "))

def operations(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operation"
should_continue = True
while should_continue:
    print(f"{a} {operation} {b} = {operations(a,b,operation)}")
    user_choice = input("Do you want to continue? Type 'yes' or 'no': ")
    if user_choice == "yes":
        a = operations(a,b,operation)
        b = int(input("Enter the next number: "))
        operation = input("Enter the operation: ")
    else:
        should_continue = False