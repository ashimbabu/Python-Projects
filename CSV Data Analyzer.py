import csv

print("===== CSV Data Analyzer =====")

file_name = input("Enter CSV file name (with .csv): ")

try:
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        rows = list(reader)

        print("\nColumn Names:", header)
        print("Total Rows:", len(rows))
        print("Total Columns:", len(header))

        # Analyze numeric column (2nd column)
        values = []
        for row in rows:
            try:
                values.append(float(row[1]))
            except:
                pass

        if values:
            print("\nData Analysis:")
            print("Minimum:", min(values))
            print("Maximum:", max(values))
            print("Sum:", sum(values))
            print("Average:", round(sum(values) / len(values), 2))
        else:
            print("No numeric data found.")

except FileNotFoundError:
    print("File not found! Please check file name.")
