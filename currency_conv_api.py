import requests
import os 
from dotenv import load_dotenv

load_dotenv() 

api_key = os.getenv("CURRENCY_API_KEY")


def convert_currency(amount, from_currency="EUR", to_currency="INR"):
    # Your API access key
    access_key = api_key
    url = "https://api.exchangerate.host/convert?from=EUR&toINR&amount=100"

    # Define the parameters
    params = {
        "access_key": api_key,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    # Send GET request to CurrencyLayer API
    response = requests.get(url, params=params)
    data = response.json()


    # Check if API call is successful
    if data.get("success"):
        result = data["result"]
        print(f"The total expenditure equivallent {amount} {from_currency} = {result:.2f} {to_currency}")
        return result
    else:
        print("Error:", data.get("error", {}).get("info", "Unknown error"))
        return None

    print(data)


