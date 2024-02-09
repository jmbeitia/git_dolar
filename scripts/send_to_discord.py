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


def make_message(data):
            
        table = "```Precios del dolar\n"
        table += "| Casa                     | Compra    | Venta     | Fecha de Actualización       |\n|--------------------------|-----------|-----------|------------------------------|\n"

        for entry in data:
            casa = entry.get("nombre")
            compra = entry.get("compra")
            venta = entry.get("venta")
            fecha_actualizacion = entry.get("fechaActualizacion")

            # Add each row to the table
            table += f"| {casa:<24} | {compra:<9} | {venta:<9} | {fecha_actualizacion:<28} |\n"
        
        table += "```"
        return table

if __name__ == "__main__":
    # Get the scraped data from the environment
    data = os.environ.get("DISCORD_MESSAGE")
    
    if not data:
        print("Error: No scraped data found.")
        sys.exit(1)

    message = make_message(data)

    # Get the Discord webhook URL from the environment variable
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("Error: Discord webhook URL not set.")
        sys.exit(1)

    send_message(webhook_url, message)
