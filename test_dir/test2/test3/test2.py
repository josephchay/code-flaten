# dummy.py

def greet(name):
    """Greet the user by name."""
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def main():
    name = input("Enter your name: ")
    print(greet(name))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")


if __name__ == "__main__":
    main()
