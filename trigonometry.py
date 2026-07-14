import math

def deg_to_rad(angle):
    return math.radians(angle)


def rad_to_deg(angle):
    return math.degrees(angle)


def sin(angle, degrees=True):
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def cos(angle, degrees=True):
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)


def tan(angle, degrees=True):
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)


def asin(value, degrees=True):
    result = math.asin(value)
    return math.degrees(result) if degrees else result


def acos(value, degrees=True):
    result = math.acos(value)
    return math.degrees(result) if degrees else result


def atan(value, degrees=True):
    result = math.atan(value)
    return math.degrees(result) if degrees else result


def sec(angle, degrees=True):
    c = cos(angle, degrees)
    if abs(c) < 1e-12:
        raise ValueError("Secant is undefined for this angle.")
    return 1 / c


def csc(angle, degrees=True):
    s = sin(angle, degrees)
    if abs(s) < 1e-12:
        raise ValueError("Cosecant is undefined for this angle.")
    return 1 / s


def cot(angle, degrees=True):
    t = tan(angle, degrees)
    if abs(t) < 1e-12:
        raise ValueError("Cotangent is undefined for this angle.")
    return 1 / t