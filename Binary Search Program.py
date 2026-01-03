print("----- Binary Search Program -----")

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


while True:
    print("\nMenu:")
    print("1. Search a Number")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        try:
            numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
            target = int(input("Enter number to search: "))
        except ValueError:
            print("Please enter valid integers only.")
            continue

        result = binary_search(numbers, target)

        if result != -1:
            print(f"Number found at position {result + 1}")
        else:
            print("Number not found in the list.")

    elif choice == 2:
        print("Binary Search Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
