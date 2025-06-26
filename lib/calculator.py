def sum(a,b): return a + b

def minus(a,b): return a - b

def multiply(a,b): return a * b

def divide(a,b):
    if b == 0:
        raise ValueError(f"Cannot divide {a} by 0")
    else:
        return a / b