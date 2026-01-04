import qrcode

print("----- QR Code Generator -----")

while True:
    print("\nMenu:")
    print("1. Generate QR Code")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        data = input("Enter text or URL to generate QR code: ")
        file_name = input("Enter file name (without .png): ")

        qr = qrcode.make(data)
        qr.save(file_name + ".png")

        print(f"QR Code generated successfully as {file_name}.png")

    elif choice == 2:
        print("QR Code Generator closed.")
        break

    else:
        print("Invalid choice. Try again.")
