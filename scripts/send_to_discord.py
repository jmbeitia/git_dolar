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

if __name__ == "__main__":
    # Get the scraped data from the environment
    message = os.environ.get("SCRAPE_DATA")
    
    if not message:
        print("Error: No scraped data found.")
        sys.exit(1)

    # Get the Discord webhook URL from the environment variable
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("Error: Discord webhook URL not set.")
        sys.exit(1)

    send_message(webhook_url, message)
