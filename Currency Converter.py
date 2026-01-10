print("===== Currency Converter =====")

# Static exchange rates (Base: NPR)
rates = {
    "NPR": 1.0,
    "USD": 0.0075,
    "EUR": 0.0069,
    "INR": 0.62
}

amount = float(input("Enter amount: "))
from_currency = input("From currency (NPR/USD/EUR/INR): ").upper()
to_currency = input("To currency (NPR/USD/EUR/INR): ").upper()

if from_currency in rates and to_currency in rates:
    # Convert to NPR first
    amount_in_npr = amount / rates[from_currency]
    
    # Convert NPR to target currency
    converted_amount = amount_in_npr * rates[to_currency]
    
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency selection!")
