import os , glob
from os import error
import logging
import pyrogram
import time
import math
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
      if count == 5:
                    message.send_sticker(chat_id,"CAACAgEAAxkBAAIC22DZazRZxcyKpsz8iNqOphiSrEdBAAJzAQACW9YqGMglMndHeNbkHgQ")
      elif count == 7 :
                    message.send_sticker(chat_id,"AgADQQYAAmMr4gk")

bughunter0.run()

