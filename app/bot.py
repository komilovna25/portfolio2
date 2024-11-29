import requests

# Telegram bot configuration
from config.settings import CHAT_ID, BOT_TOKEN

def send_message(text):
    """
    Send a message to a Telegram bot using the bot's token and a predefined chat ID.
    """
    BOT_TOKENs = BOT_TOKEN
    CHAT_IDs = CHAT_ID
    PHOTO = "https://cdn.create.vista.com/api/media/small/223453354/stock-photo-cropped-shot-businesspeople-working-workplace-digital-devices-documents"
    
    # The URL to send the message
    url = f"https://api.telegram.org/bot{BOT_TOKENs}/sendphoto?chat_id={CHAT_IDs}&photo={PHOTO}&caption={text}"

    # Send the message using a GET request (you can use POST as well if you prefer)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully to Telegram bot!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
