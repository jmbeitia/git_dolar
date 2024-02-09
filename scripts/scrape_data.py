import requests
import os

def get_dolar_values():
    url = "https://dolarapi.com/v1/dolares"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response

        data = response.json()

        return data

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return "Unable to fetch Dolar values."

if __name__ == "__main__":
    data = get_dolar_values()

    print(data)
