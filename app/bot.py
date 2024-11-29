import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://cdn.create.vista.com/api/media/small/223453354/stock-photo-cropped-shot-businesspeople-working-workplace-digital-devices-documents"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  response = requests.get(url)