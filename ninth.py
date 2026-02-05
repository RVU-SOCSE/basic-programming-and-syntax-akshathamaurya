# TEMP CONVERTER
#akshatha r
#usn-1RUA25BCA0009

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '3':
        print("Exiting converter...")
        break

    temp = float(input("Enter temperature value: "))

    match choice:
        case '1':
            result = (temp * 9/5) + 32
            print("Temperature in Fahrenheit =", result)

        case '2':
            result = (temp - 32) * 5/9
            print("Temperature in Celsius =", result)

        case _:
            print("Invalid choice! Please select between 1 and 3.")
