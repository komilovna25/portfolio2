import requests

from config.settings import CHAT_ID, BOT_TOKEN

def send_message(text):
    """
    Send a message to a Telegram bot using the bot's token and a predefined chat ID.
    """
    BOT_TOKENs = BOT_TOKEN
    CHAT_IDs = CHAT_ID
    PHOTO = "https://cdn.create.vista.com/api/media/small/223453354/stock-photo-cropped-shot-businesspeople-working-workplace-digital-devices-documents"
    
    url = f"https://api.telegram.org/bot{BOT_TOKENs}/sendphoto?chat_id={CHAT_IDs}&photo={PHOTO}&caption={text}"

    response = requests.get(url)

 
    if response.status_code == 200:
        print("Message sent successfully to Telegram bot!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
