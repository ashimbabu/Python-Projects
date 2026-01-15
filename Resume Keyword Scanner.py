print("===== Resume Keyword Scanner =====")

# Predefined job keywords (can be changed)
job_keywords = [
    "python", "machine learning", "data analysis",
    "sql", "gis", "remote sensing", "deep learning",
    "statistics", "ai", "geoai", "data science"
]

try:
    file_name = input("Enter resume file name (example: resume.txt): ")

    with open(file_name, "r") as file:
        resume_text = file.read().lower()

    matched_keywords = []
    missing_keywords = []

    for keyword in job_keywords:
        if keyword in resume_text:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    total_keywords = len(job_keywords)
    matched_count = len(matched_keywords)
    match_percentage = (matched_count / total_keywords) * 100

    print("\n===== Scan Result =====")
    print(f"Total Keywords: {total_keywords}")
    print(f"Matched Keywords: {matched_count}")
    print(f"Match Percentage: {match_percentage:.2f}%")

    print("\nMatched Keywords:")
    for k in matched_keywords:
        print("-", k)

    print("\nMissing Keywords:")
    for k in missing_keywords:
        print("-", k)

except FileNotFoundError:
    print("Error: Resume file not found. Please check the file name.")
