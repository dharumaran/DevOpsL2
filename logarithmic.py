import math

def natural_log(x):
    """Calculates the natural logarithm (base e) of x."""
    if x <= 0:
        return "Error: Logarithm undefined for zero or negative values."
    return math.log(x)

def base_10_log(x):
    """Calculates the common logarithm (base 10) of x."""
    if x <= 0:
        return "Error: Logarithm undefined for zero or negative values."
    return math.log10(x)

def custom_base_log(x, base):
    """Calculates the logarithm of x with a custom base."""
    if x <= 0:
        return "Error: Logarithm undefined for zero or negative values."
    if base <= 0 or base == 1:
        return "Error: Base must be greater than 0 and not equal to 1."
    return math.log(x, base)