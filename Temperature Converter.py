print("========== Temperature Converter ==========")

while True:
    print("\nChoose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F = {celsius}°C")

    elif choice == "3":
        print("Temperature Converter closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
