import os 
from os import error
import logging
import pyrogram
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document

    
bughunter0 = Client(
    "Member-Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING = """ Hi {}, I'm Sticker Bot. 
Sends Relevant Thankyou Sticker in Groups and Channel"""


JOIN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')
        ]]
    )

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_STRING.format(update.from_user.mention)
    reply_markup = JOIN_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message(filters.command(["ping"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@bughunter0.on_message(filters.new_chat_members & (filters.group | filters.channel))
async def sticker(bot, message):
      chat_id = str(message.chat.id)
      count = await bughunter0.get_chat_members_count(chat_id)
      if count == 3:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAJvHmDbM3JkdZxptNLZ5fsMkfx0ldRyAAL1AgACufE4VgHHxPJeyWOKHgQ")
      elif count == 5:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 7:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 10:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 25:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 30:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALABWDbNB7gPjkDzwtQ6Cs5nvhb0wwZAAJzAQACW9YqGMglMndHeNbkIAQ")
      elif count == 35:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAH2DbNKfjQOZnjBt6v7Ec2gQiw73XAALDAgACdhE4VlXq3LxwIYXVIAQ")
      elif count == 40:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALABmDbNB4JXht6BxaWYeZBEbrCXTm7AAJ1AQACW9YqGAqMjpiJaz52IAQ")
      elif count == 45:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 50:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 55:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAImDbNKjVte3znXJlKUKAWNppbLFdAAJSAwACI9U5VugjgalV5M1EIAQ")
      elif count == 60:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 65:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAJGDbNKnFe63T7dvQNpo3fQzJ3ByRAAKjBAAC2DoxVo0AAfZxo3XDXiAE")
      elif count == 70:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 75:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 80:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALADmDbNEky6eEvIdpeoFeyej1ITyjHAAJ9AQACW9YqGIGH0t8XkK5rIAQ")
      elif count == 85:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 90:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAKGDbNKxw5kOeM5vIuJNVhc8QfdyvAAJDBAACVQk5VkLLUBVbCmAFIAQ")
      elif count == 95:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 99:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAKmDbNK493tFvInPAZbRkRxI7A94mAAK8AwACeFQ4VoQ3RqKdVqA-IAQ")
      elif count == 100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAR2DbNZK1cN3x1puKuLpFV7eELnLGAAKBAQACW9YqGJuh7P1hvjLlIAQ")
      elif count == 110:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 120:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAWmDbNkJveb8bEh9AmgRmnaLwv7sMAAKRAwACnOo4VjyzYcbK44llIAQ")
      elif count == 130:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 140:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 150:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALASWDbNZTcEdbBZLDTWJUUyI28t8GFAAKDAQACW9YqGCcn5HlB2BFHIAQ")
      elif count == 160:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAXWDbNkZQifrUCZuiDVbgzVFUv3ZdAAIDAwACf7k5VsRb3FPkL5P2IAQ")
      elif count == 170:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 180:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAX2DbNkfJxEL9LCFjlPnmP2wuQteHAAIuBAACS0k5Vi96vtzMVBELIAQ")
      elif count == 190:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 199:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAS2DbNZVlilesDRpcaTHL8xxE7vSLAAKFAQACW9YqGGcqtjuLAj1EIAQ")
      elif count == 210:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      






bughunter0.run()

