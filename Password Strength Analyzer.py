import re

print("===== Password Strength Analyzer =====")

password = input("Enter your password: ")

strength = 0
suggestions = []

# Length check
if len(password) >= 8:
    strength += 1
else:
    suggestions.append("Use at least 8 characters")

# Uppercase check
if re.search(r"[A-Z]", password):
    strength += 1
else:
    suggestions.append("Add uppercase letters")

# Lowercase check
if re.search(r"[a-z]", password):
    strength += 1
else:
    suggestions.append("Add lowercase letters")

# Digit check
if re.search(r"[0-9]", password):
    strength += 1
else:
    suggestions.append("Add numbers")

# Special character check
if re.search(r"[!@#$%^&*()_+]", password):
    strength += 1
else:
    suggestions.append("Add special characters (!@#$...)")

# Result
print("\nPassword Analysis")
print("-----------------")

if strength == 5:
    print("Strength: Very Strong 🔐")
elif strength == 4:
    print("Strength: Strong")
elif strength == 3:
    print("Strength: Medium")
else:
    print("Strength: Weak ❌")

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
