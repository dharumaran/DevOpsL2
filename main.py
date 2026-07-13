from operations import add, subtract, multiply, divide

# Dictionary of available operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def display_menu():
    print("\n===== Calculator =====")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("q : Quit")


while True:
    display_menu()

    choice = input("Choose an operation: ")

    if choice.lower() == "q":
        print("Goodbye!")
        break

    if choice not in operations:
        print("Invalid operation.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    result = operations[choice](a, b)

    print("Result:", result)