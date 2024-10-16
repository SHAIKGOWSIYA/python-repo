def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is undefined"

if __name__ == "__main__":
    x = 10
    y = 5
    print(f"Addition: {addition(x, y)}")
    print(f"Subtraction: {subtraction(x, y)}")
    print(f"Multiplication: {multiplication(x, y)}")
    print(f"Division: {division(x, y)}")
