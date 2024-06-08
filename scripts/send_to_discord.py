import sys
import os
import requests


def send_message(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


def get_dolar_values():
    short_forms = {
        "Oficial": "Ofic",
        "Blue": "Blue",
        "Bolsa": "Bols",
        "Contado con liquidación": "CCL",
        "Mayorista": "Mayo",
        "Cripto": "Crip",
        "Tarjeta": "Tarj"
    }
    url = "https://dolarapi.com/v1/dolares"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response

        data = response.json()

        table = "```\n| Casa | Comp | Vent |\n|------|------|------|\n"

        for entry in data:
            casa = short_forms[entry.get("nombre")]
            compra = int(entry.get("compra"))
            venta = int(entry.get("venta"))

            table += f"| {casa:<4} | {compra:<4} | {venta:<4} |\n"

        table += "```"
        return table

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return "Unable to fetch the Dolar values."


if __name__ == "__main__":
    # Get the scraped data from the environment
    message = get_dolar_values()

    # Get the Discord webhook URL from the environment variable
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Error: Discord webhook URL not set.")
        sys.exit(1)

    send_message(webhook_url, message)
