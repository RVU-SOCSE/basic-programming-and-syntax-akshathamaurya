#simple calculator
#akshatha r
#usn-1RUA25BCA0009

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            print("Result =", num1 + num2)

        case '2':
            print("Result =", num1 - num2)

        case '3':
            print("Result =", num1 * num2)

        case '4':
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")

        case _:
            print("Invalid choice! Please select between 1 and 5.")
