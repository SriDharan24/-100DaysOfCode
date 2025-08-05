# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero!"
    return x / y

def main():
    print("🧮 Welcome to the Python Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("❌ Invalid choice.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    if choice == '1':
        print(f"✅ Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"✅ Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"✅ Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"✅ Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
