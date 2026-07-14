from operations import add, subtract, multiply, divide
import logarithmic  # Importing your module
import ExpOps
import logarithmic
import trigonometry

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "ln": logarithmic.natural_log,
    "log10": logarithmic.base_10_log,
    "log": logarithmic.custom_base_log,
    "sin": trigonometry.sin,
    "cos": trigonometry.cos,
    "tan": trigonometry.tan,
    "asin": trigonometry.asin,
    "acos": trigonometry.acos,
    "atan": trigonometry.atan,
    "sec": trigonometry.sec,
    "csc": trigonometry.csc,
    "cot": trigonometry.cot,
    "deg2rad": trigonometry.deg_to_rad,
    "rad2deg": trigonometry.rad_to_deg,
    "twopowerx": ExpOps.twoPowerX,
    "power":ExpOps.power,
    "exponential":ExpOps.exp
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
    print("sin    : Sine")
    print("cos    : Cosine")
    print("tan    : Tangent")
    print("asin   : Inverse Sine")
    print("acos   : Inverse Cosine")
    print("atan   : Inverse Tangent")
    print("sec    : Secant")
    print("csc    : Cosecant")
    print("cot    : Cotangent")
    print("deg2rad: Degrees to Radians")
    print("rad2deg: Radians to Degrees")
    print("q   : Quit")
   


while True:
    display_menu()

    choice = input("Choose an operation: ").strip()
    choice=choice.lower()

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
        elif choice in ["ln", "log10"]:
            a = float(input("Enter number: "))
            result = operations[choice](a)

        elif choice == "log":
            a = float(input("Enter number: "))
            base = float(input("Enter base: "))
            result = operations[choice](a, base)

        elif choice in [
            "sin", "cos", "tan",
            "asin", "acos", "atan",
            "sec", "csc", "cot",
            "deg2rad", "rad2deg"
        ]:
            a = float(input("Enter angle/value: "))
            result = operations[choice](a)

        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = operations[choice](a, b)

    except ValueError as e:
        print(e)
        continue

    print("Result:", result)