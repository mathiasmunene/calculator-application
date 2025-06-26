from lib.calculator import sum, minus, multiply, divide 
from lib.quotes import get_todays_random_quote


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
                if choice == '1':                    
                    result = sum(a, b)
                    print(f"{a} + {b} = {result}")
                elif choice == '2':
                    result = minus(a, b)
                    print(f"{a} - {b} = {result}")
                elif choice == '3':
                    result = multiply(a, b)
                    print(f"{a} * {b} = {result}")
                elif choice == '4':
                    result = divide(a, b)
                    print(f"{a} / {b} = {result}")
            except ValueError as e:
                print("Invalid input:", e)
        elif choice == '5':
            quote = get_todays_random_quote()
            print(quote['quote'])
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid Input:", choice)

if __name__ == "__main__":
    main()

# TOML - Tom's Obvious Minimal Language