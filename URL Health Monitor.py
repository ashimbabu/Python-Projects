import requests
import time

print("===== URL Health Monitor =====")

urls = []

n = int(input("How many URLs do you want to monitor? "))

for i in range(n):
    url = input(f"Enter URL {i+1}: ")
    urls.append(url)

print("\nChecking URL status...\n")

for url in urls:
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()

        response_time = end_time - start_time

        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:
            print("Status: UP ✅")
        else:
            print("Status: DOWN ⚠️")

        print("-" * 40)

    except requests.exceptions.RequestException:
        print(f"URL: {url}")
        print("Status: DOWN ❌ (Not reachable)")
        print("-" * 40)
