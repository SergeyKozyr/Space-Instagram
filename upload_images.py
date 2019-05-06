import os
from instabot import Bot
from dotenv import load_dotenv


load_dotenv()
bot = Bot()
bot.login(username=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
image_directory = os.listdir('./images')
for image in image_directory:
    bot.upload_photo(f'./images/{image}')
