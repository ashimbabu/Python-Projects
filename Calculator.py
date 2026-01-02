print("............Calculator............")
print("............calculator............")

"""
addition, substraction, multiplication, division, reminder, power, quotient, even/odd,
"""

while True :
    print("............calculator............")
    print("choose your operation: \n")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Reminder (%)")
    print("6. Power (**)")
    print("7. Quotient (//)")
    print("8. Even/odd check")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 9:
        print("Calculator closed")
        break #terminate the loop and exit 

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if choice == 1:
        add = n1 + n2
        print(f"Addition result is {add} ")

    elif choice == 2:
        sub = n1 - n2
        print(f"Substraction result is {sub} ")

    elif choice == 3:
        multiply = n1 * n2
        print(f"Substraction result is {multiply} ")

    elif choice == 4:
        division = n1/n2
        print(f"Substraction result is {division} ")

    elif choice == 5:
        reminder = n1 % n2
        print(f"Reminder result is {reminder} ")
        
    elif choice == 6:
        power = n1 ** n2
        print(f"Power result is {power} ")

    elif choice == 7:
        quotient = n1 // n2
        print(f"Quotion result is {quotient} ")

    elif choice == 8:
        
        if n1 % 2 == 0:
            print(f"{n1} is an even number")
        else:
            print(f"{n1} is an odd number")
        
        if n2 % 2 == 0:
            print(f"{n1} is an even number")
        else:
            print(f"{n1} is an odd number")

else:
    print(" Please try again. Your choice is invalid.")
            