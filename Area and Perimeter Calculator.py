print("----- Area and Perimeter Calculator -----")

while True:
    print("\nChoose a shape:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        length = float(input("Enter length of rectangle: "))
        breadth = float(input("Enter breadth of rectangle: "))

        area = length * breadth
        perimeter = 2 * (length + breadth)

        print(f"Area of Rectangle = {area}")
        print(f"Perimeter of Rectangle = {perimeter}")

    elif choice == "2":
        side = float(input("Enter side of square: "))

        area = side * side
        perimeter = 4 * side

        print(f"Area of Square = {area}")
        print(f"Perimeter of Square = {perimeter}")

    elif choice == "3":
        radius = float(input("Enter radius of circle: "))
        pi = 3.1416

        area = pi * radius * radius
        perimeter = 2 * pi * radius

        print(f"Area of Circle = {area}")
        print(f"Perimeter (Circumference) of Circle = {perimeter}")

    elif choice == "4":
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        side1 = float(input("Enter first side of triangle: "))
        side2 = float(input("Enter second side of triangle: "))
        side3 = float(input("Enter third side of triangle: "))

        area = 0.5 * base * height
        perimeter = side1 + side2 + side3

        print(f"Area of Triangle = {area}")
        print(f"Perimeter of Triangle = {perimeter}")

    elif choice == "5":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
