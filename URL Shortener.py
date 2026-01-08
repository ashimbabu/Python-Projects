import hashlib
import os

print("===== URL Shortener =====")

DATA_FILE = "urls.txt"

# Create file if not exists
if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()

def generate_short_code(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]

def shorten_url():
    long_url = input("Enter long URL: ").strip()

    with open(DATA_FILE, "r") as f:
        for line in f:
            code, stored_url = line.strip().split(",")
            if stored_url == long_url:
                print(f"Short URL code already exists: {code}")
                return

    short_code = generate_short_code(long_url)

    with open(DATA_FILE, "a") as f:
        f.write(f"{short_code},{long_url}\n")

    print(f"Short URL created: http://short.ly/{short_code}")

def retrieve_url():
    short_code = input("Enter short code: ").strip()
    with open(DATA_FILE, "r") as f:
        for line in f:
            code, url = line.strip().split(",")
            if code == short_code:
                print(f"Original URL: {url}")
                return
    print("Short URL not found!")

while True:
    print("\nMenu:")
    print("1. Shorten URL")
    print("2. Retrieve Original URL")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        shorten_url()
    elif choice == "2":
        retrieve_url()
    elif choice == "3":
        print("URL Shortener closed.")
        break
    else:
        print("Invalid choice.")
