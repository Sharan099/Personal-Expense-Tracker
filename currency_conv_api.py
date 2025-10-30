import requests

def convert_currency(amount, from_currency="EUR", to_currency="INR"):
    # Your API access key
    access_key = "15dd497a3197675fa5d1bdf2e4bad0e6"
    url = "https://api.exchangerate.host/convert?from=EUR&toINR&amount=100"

    # Define the parameters
    params = {
        "access_key": access_key,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    # Send GET request to CurrencyLayer API
    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    # Check if API call is successful
    if data.get("success"):
        result = data["result"]
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        return result
    else:
        print("Error:", data.get("error", {}).get("info", "Unknown error"))
        return None


