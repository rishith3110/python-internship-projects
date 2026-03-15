import re

password = input("Enter your password: ")

score = 0
missing = []

if len(password) >= 8:
    score += 1
else:
    missing.append("Minimum 8 characters")

if re.search("[A-Z]", password):
    score += 1
else:
    missing.append("Uppercase letter")

if re.search("[a-z]", password):
    score += 1
else:
    missing.append("Lowercase letter")

if re.search("[0-9]", password):
    score += 1
else:
    missing.append("Number")

if re.search("[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
    score += 1
else:
    missing.append("Special character")

print("\nPassword Analysis : ")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

if missing:
    print("Missing requirements:")
    for item in missing:
        print("-", item)
else:
    print("Your password meets all requirements!")