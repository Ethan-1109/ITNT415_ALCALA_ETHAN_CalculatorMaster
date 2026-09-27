def add(a, b):
    return a + b

def subtract(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def print_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = add(num1, num2)
        print(f"Result: {result}")
    else:
        print("That option isn't built yet on this branch.")

if __name__ == "__main__":
    main()

