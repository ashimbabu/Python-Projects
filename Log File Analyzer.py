print("===== Log File Analyzer =====")

file_name = input("Enter log file name (with .log or .txt): ")

info_count = 0
warning_count = 0
error_count = 0
error_messages = {}

try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("INFO"):
                info_count += 1
            elif line.startswith("WARNING"):
                warning_count += 1
            elif line.startswith("ERROR"):
                error_count += 1
                message = line[6:]  # Remove 'ERROR '
                error_messages[message] = error_messages.get(message, 0) + 1

    print("\nLog Analysis Report")
    print("--------------------")
    print("INFO messages   :", info_count)
    print("WARNING messages:", warning_count)
    print("ERROR messages  :", error_count)

    if error_messages:
        most_common_error = max(error_messages, key=error_messages.get)
        print("\nMost Frequent Error:")
        print(most_common_error)
    else:
        print("\nNo error messages found.")

except FileNotFoundError:
    print("Log file not found. Please check the file name.")
