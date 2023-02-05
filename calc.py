def add(num1, num2):
    """Add Function"""
    return num1 + num2


def subtract(num1, num2):
    """Subtract Function"""
    return num1 - num2


def multiply(num1, num2):
    """Multiply Function"""
    return num1 * num2


def divide(num1, num2):
    """Divide Function"""
    if num2 == 0:
        raise ValueError('Can not be zero!')
    return num1 / num2
