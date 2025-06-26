def main():
    print("Welcome to the CLI Calculator!")

    while True:
        print("1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit")   
        choice = input("Choose an operation: ")

        if choice in ['1', '2', '3', '4']:
            #operation
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
        elif choice == '5':
            break
        else:
            print("Invalid Input:", choice)