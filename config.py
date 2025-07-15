#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "16995961")
API_HASH = os.environ.get("API_HASH", "8817a7d4293049593e60999359970ddd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7852987763:AAFh5Bb1OoxJbWJq9TksDDomUw9FTHw_sWA")
ADMIN = int(os.environ.get("ADMIN", '7364106679'))
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://envs.sh/u0Z.jpg/IMG20250701161.jpg" # Replace with your Telegraph link - Start Pic
INFO_PIC= "https://envs.sh/u05.jpg/IMG20250701173.jpg" # Replace with your Telegraph link - Information 
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "https://t.me/Toon_Encodes_Telugu") # Replace with your Updates link
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/forcesubnothingboy") # Replace with your Support link
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080")) #for koyeb 8080 only
