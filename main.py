from operations import add, subtract, multiply, divide
import logarithmic  # Importing your module
import ExpOps

# Dictionary of available operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "ln": logarithmic.natural_log,
    "log10": logarithmic.base_10_log,
    "log": logarithmic.custom_base_log,
    "TwoPowerX":ExpOps.twoPowerX,
    "Power":ExpOps.power,
    "Exponential": ExpOps.exp

}

def display_menu():
    print("\n===== Calculator =====")
    print("+   : Addition")
    print("-   : Subtraction")
    print("* : Multiplication")
    print("/   : Division")
    print("ln  : Natural Logarithm (base e)")
    print("log10: Common Logarithm (base 10)")
    print("log : Custom Base Logarithm")
    print("twopowerx: 2^x")
    print("power: x^y")
    print("exponential: e^x")
    print("q   : Quit")


while True:
    display_menu()

    choice = input("Choose an operation: ").strip()

    if choice.lower() == "q":
        print("Goodbye!")
        break

    if choice not in operations:
        print("Invalid operation.")
        continue

    try:
        # Handle Logarithmic operations (which only need 1 or specific custom inputs)
        if choice in ["ln", "log10","twopowerx","exponential"]:
            a = float(input("Enter number: "))
            result = operations[choice](a)
            
            
        # Handle standard arithmetic operations (which need 2 numbers)
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = operations[choice](a, b)
            
    except ValueError:
        print("Please enter valid numbers.")
        continue

    print("Result:", result)