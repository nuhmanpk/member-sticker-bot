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
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAcWDbNvSOrJU6oRg29s6IYp0zT04PAAJ1AgACb8FkFDCUuHcEvpgrIAQ")
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
      elif count == 225:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 250:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 275:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 300:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 325:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 350:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 375:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 400:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 425:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 450:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 475:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAj2DbOcy9R31WJyH6BxJj1Aq0DOH3AAKQAQACW9YqGJcbNF6RK3NUIAQ")
      elif count == 500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAkGDbOc3bdFb9rMO3uwEAAereBZR0pwACkQEAAlvWKhgDp1k6OPv46CAE")
      elif count == 525:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 550:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 575:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAq2DbOmb9FUwkATVDYAlhsFOmMcF5AAKUAQACW9YqGCvPzoMmogIiIAQ")
      elif count == 600:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 625:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 650:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 675:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAsGDbOmmshfdpwmCSryBchmoK3yTxAAKZAQACW9YqGPTEWeDhdOVOIAQ")
      elif count == 725:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 750:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAsmDbOmrNDjq0yIr3eWCoIy91syzpAAKbAQACW9YqGOtGZWA98zCaIAQ")
      elif count == 775:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAs2DbOmsuO7u5AdPO9TPF1XW5n8rOAAKcAQACW9YqGFETXctTCf3dIAQ")
      elif count == 800:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 825:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 850:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 875:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 900:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 925:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 950:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 975:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAu2DbOnBUZ5DFwavvXo3Zq6hX5GrZAAKkAQACW9YqGGzROjV9WdVBIAQ")
      elif count == 1000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAvGDbOnFkRPePdhEWXBwTSV4eJfjTAAKlAQACW9YqGAluL79s0KEQIAQ")
      elif count == 1100:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 1200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA6WDbO1TxfZyF69PzmCw7nsrB2LDvAAKnAQACW9YqGEVp0JPc4nO6IAQ")
      elif count == 1300:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 1400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA62DbO1YL1arJf9zVgdTGIVB7MUGhAAKpAQACW9YqGAWw3fw07KjYIAQ")
      elif count == 1500:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 1600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA7WDbO1jGcxdqGAVsFhsXKoMp1epDAAKrAQACW9YqGLsCrwgNIGYkIAQ")
      elif count == 1700:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 1800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA72DbO1jWqU4PWKin9Bp9YEAZVnqQAAKtAQACW9YqGKEnAe3tZlvHIAQ")
      elif count == 1900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8GDbO1lPUheD5q2KRr1E0ue07bVGAAKuAQACW9YqGOq5CMnZqqvdIAQ")
      elif count == 2000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8WDbO1lSjFdU0zOJsCxglr41pTVOAAKvAQACW9YqGPFJNraaGLBkIAQ")
      elif count == 2100:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 2200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQmDbPPPsIgABUtrgFfZsu7GdAAEUxQYAArEBAAJb1ioYog7dqaYf2M0gBA")
      elif count == 2300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQ2DbPPRsp7QrM-wQBgHBb0SZzl13AAKyAQACW9YqGDH2xakhpikbIAQ")
      elif count == 2400:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 2500:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 2600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBRmDbPPXuU7h3tgaF1PEGHUtR4jp0AAK1AQACW9YqGIrf25Ws6cZgIAQ")
      
      elif count == 2700:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 2800:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 2900:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBOmDbPKJTEw96snijk3zWDju5o0cwAAK5AQACW9YqGNTV9iTuJqtXIAQ")
      elif count == 3100:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3200:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3300:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3400:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3500:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3600:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3700:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3800:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 3900:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 4000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 4100:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 4200:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      





bughunter0.run()

