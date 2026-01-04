from PIL import Image, ImageFilter

print("----- Photo Manipulation App -----")

while True:
    print("\nMenu:")
    print("1. Open and Edit Image")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ").strip()
    if choice == "1":
        path = input("C:/Users/acer/Desktop/Python-Projects: ").strip()
        try:
            img = Image.open(path)
        except:
            print("Error! File not found or invalid format.")
            continue

        print("\nEditing options:")
        print("1. Convert to Grayscale")
        print("2. Rotate Image")
        print("3. Resize Image")
        print("4. Blur Image")
        print("5. Save Image")

        while True:
            option = input("Choose option (1-5) or 'back' to return to main menu: ").strip()
            
            if option == "1":
                img = img.convert("L")
                img.show()
            elif option == "2":
                angle = int(input("Enter rotation angle (degrees): "))
                img = img.rotate(angle)
                img.show()
            elif option == "3":
                width = int(input("Enter new width: "))
                height = int(input("Enter new height: "))
                img = img.resize((width, height))
                img.show()
            elif option == "4":
                img = img.filter(ImageFilter.BLUR)
                img.show()
            elif option == "5":
                save_path = input("Enter file name to save (with extension, e.g., output.jpg): ")
                img.save(save_path)
                print(f"Image saved as {save_path}")
            elif option.lower() == "back":
                break
            else:
                print("Invalid option. Try again.")

    elif choice == "2":
        print("Photo Manipulation App closed.")
        break
    else:
        print("Invalid choice. Try again.")
