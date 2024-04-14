# /usr/bin/nuhman/bughunter0 

import os 
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document, ChatMember
from sticker import stickers
    
bughunter0 = Client(
    "Member-Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING_PRIVATE = """ Hi {}, I'm Member Sticker Bot. 
 I Can Send Relevant Thankyou Sticker in Groups and Channel
\n All Member count doesn't return a sticker, so I will send a Thank you message for the count which have no sticker,
This message will be deleted after 10 second. \n
Nothing to Do here !! 😕
**ADD ME TO A GROUP THEN TRIGGER ME**
"""

START_STRING_GROUP = """ **I need Admin rights to Send sticker in {}**

`Join My Updates Channel for Getting more familiar with me`

"""

ABOUT = """
● **BOT:** `Member Sticker BOT` 
● **AUTHOR :** [bughunter0](https://t.me/bughunter0) 
● **SERVER :** `Heroku` 
● **LIBRARY :** `Pyrogram` 
● **LANGUAGE :** `Python 3.9` 
● **SOURCE :** [BugHunterBots](https://t.me/BugHunterBots/93) 

"""
HELP = """
● Still Wonder How I Work ? 
● Use /How get a Full Brief
● Use /Donate to Donate
"""


CHANNEL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')
        ]]
    )
ADDME_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ ADD ME TO A GROUP ↗', url="t.me/member_sticker_bot?startgroup=true")
        ]]
    )
START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ABOUT',callback_data='cbabout'),
        InlineKeyboardButton('HELP',callback_data='cbhelp')
        ],
        [
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots'),
        ],
        [InlineKeyboardButton('↗ ADD ME TO A GROUP ↗', url="t.me/member_sticker_bot?startgroup=true")
        ]]
        
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back',callback_data='cbclose'),
        ]]
    )

@bughunter0.on_callback_query() # callbackQuery()
async def cb_data(bot, update):  
    if update.data == "cbhelp":
        await update.message.edit_text(
            text=HELP,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "cbabout":
        await update.message.edit_text(
            text=ABOUT,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.edit_text(
            text=START_STRING_PRIVATE.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTON
        )


@bughunter0.on_message(filters.command(["start"]) & filters.private)
async def start_private(bot, update):
    text = START_STRING_PRIVATE.format(update.from_user.mention)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message((filters.command(["start"]) & filters.group) | filters.regex("/start@member_sticker_bot"))
async def start_group(bot, update):
    text = START_STRING_GROUP.format(update.chat.title)
    reply_markup = CHANNEL_BUTTON
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

@bughunter0.on_message(filters.new_chat_members & filters.group)
async def sticker_group(bot, message):
   try:
      chat_id = int(message.chat.id)
      count = await bughunter0.get_chat_members_count(chat_id)
      if count in stickers:
        await bot.send_sticker(chat_id, stickers[count])
      else : 
            txt = await message.reply_text(f"**We are Happy to Have you as Our** `{count} th Member`")
           
           
            
   except Exception as error:
            await message.reply("@admins , \nAs per Your Group Permission Members of This Group Can't send Stickers to this Chat (`I'm a Member, Not an Admin`) .\n**To Solve this Issue add me as Admin Or Give permission to send stickers in the Chat** \n\n\n ©@BugHunterBots")


@bughunter0.on_message(filters.channel & filters.command(["start"]))
async def sticker_channel(bot, message):
 chat_id = int(message.chat.id)
 await bot.send_message(text="We Are Working On It",chat_id=chat_id)
 



@bughunter0.on_message(filters.command(["help"]))
async def help(bot, message):
 chat_id = str(message.chat.id)
 await bot.send_sticker(chat_id,"CAACAgIAAxkBAAEEDq1g6Y5LLm2DtFwCV2pPNCddwwZQHgAC6AkAAowucAABsFGHedLEzeUgBA")  
 


bughunter0.run()

