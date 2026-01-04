import requests

print("----- Weather Forecast App -----")

API_KEY = "277b5b287fb22dc1092590589dbdba28"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    print("\nMenu:")
    print("1. Check Weather")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Enter 1 or 2.")
        continue

    if choice == 1:
        city = input("Enter city name: ").strip()
        if not city:
            print("City name cannot be empty.")
            continue

        # Use country code NP to ensure Kathmandu, Nepal
        url = f"{BASE_URL}?q=Kathmandu,NP&appid={"277b5b287fb22dc1092590589dbdba28"}&units=metric"

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            if response.status_code != 200:
                print(f"Error: {data.get('message', 'City not found')}")
                continue

            print(f"\nWeather in {city}:")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']} %")
            print(f"Wind Speed: {data['wind']['speed']} m/s")

        except requests.exceptions.RequestException as e:
            print("Network error:", e)

    elif choice == 2:
        print("Weather App closed.")
        break
    else:
        print("Invalid choice. Try again.")

