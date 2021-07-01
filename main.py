import os 
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document, ChatMember

    
bughunter0 = Client(
    "Member-Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING_PRIVATE = """ Hi {}, I'm Member Sticker Bot. 
 I Can Sends Relevant Thankyou Sticker in Groups and Channel
Nothing to Do here !! ADD ME TO A GROUP THEN TRIGGER ME
"""

START_STRING_GROUP = """ **I need Admin rights to Send sticker in {},**

`If Done Neglect it !!`

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


@bughunter0.on_message(filters.command(["start"]) & filters.private)
async def start_private(bot, update):
    text = START_STRING_PRIVATE.format(update.from_user.mention)
    reply_markup = ADDME_BUTTON
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

@bughunter0.on_message(filters.new_chat_members & (filters.group | filters.channel))
async def sticker(bot, message):
      chat_id = str(message.chat.id)
      count = await bughunter0.get_chat_members_count(chat_id)
      if count == 3:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAJvHmDbM3JkdZxptNLZ5fsMkfx0ldRyAAL1AgACufE4VgHHxPJeyWOKHgQ")
      elif count == 5:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAID32DbTvj4x1EqZGtgqFd0ZTwmpgUqAAKQAgACCoU4Vh4T1CeHhp9dHgQ")
      elif count == 7:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAID4mDbTx5XeQc2RtMFW6exz6Mt34OBAALdAgAC7f84ViojLrLihZXFHgQ")
      elif count == 10:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIDyWDbTa8QqPLlVGN22VI0M7Pr0nqMAALdAgAC7f84ViojLrLihZXFHgQ")
      elif count == 25:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAcWDbNvSOrJU6oRg29s6IYp0zT04PAAJ1AgACb8FkFDCUuHcEvpgrIAQ")
      elif count == 30:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALABWDbNB7gPjkDzwtQ6Cs5nvhb0wwZAAJzAQACW9YqGMglMndHeNbkIAQ")
      elif count == 35:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAH2DbNKfjQOZnjBt6v7Ec2gQiw73XAALDAgACdhE4VlXq3LxwIYXVIAQ")
      elif count == 40:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALABmDbNB4JXht6BxaWYeZBEbrCXTm7AAJ1AQACW9YqGAqMjpiJaz52IAQ")
      elif count == 45:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAID52DbT5z5vwwcS0bRUWoAARhw2JfYbQACvAMAAgiqMVak26ZzJPzEEx4E")
      elif count == 50:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIED2DbUA8YaVbYncLCyKBD80VrysOgAAJ2AgACb8FkFMQhQH7icivgHgQ")
      elif count == 55:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAImDbNKjVte3znXJlKUKAWNppbLFdAAJSAwACI9U5VugjgalV5M1EIAQ")
      elif count == 60:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEG2DbUGZC2tESsD4l4yOS2VDAV05wAAJNAgACKrU4VuCu1cQtX77xHgQ")
      elif count == 65:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAJGDbNKnFe63T7dvQNpo3fQzJ3ByRAAKjBAAC2DoxVo0AAfZxo3XDXiAE")
      elif count == 70:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEIGDbULCpwfKGQuXjW7izn30LmKQsAAJIAgACE1g5VsL7ptwX608LHgQ")
      elif count == 75:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEIWDbUJgYjt4nVaK2TN9ILxXE7AprAAJ3AgACb8FkFNnvojLmMWChHgQ")
      elif count == 80:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALADmDbNEky6eEvIdpeoFeyej1ITyjHAAJ9AQACW9YqGIGH0t8XkK5rIAQ")
      elif count == 85:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEKmDbUNQuux2Hp6IU3L1QqWEutHvsAALYAgACzj0xVoeTUX9wbijPHgQ")
      elif count == 90:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAKGDbNKxw5kOeM5vIuJNVhc8QfdyvAAJDBAACVQk5VkLLUBVbCmAFIAQ")
      elif count == 95:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEMWDbUPd1dWP5x33XBfo0Xzgs82MXAAIqAwACij05VhffSZgbF5LwHgQ")
      elif count == 99:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAKmDbNK493tFvInPAZbRkRxI7A94mAAK8AwACeFQ4VoQ3RqKdVqA-IAQ")
      elif count == 100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAR2DbNZK1cN3x1puKuLpFV7eELnLGAAKBAQACW9YqGJuh7P1hvjLlIAQ")
      elif count == 110:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIENGDbURGU5UU7f6hy8KPX6ttQZRZwAAIQAwAC9Cg5VmTUQm6kaO9mHgQ")
      elif count == 120:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAWmDbNkJveb8bEh9AmgRmnaLwv7sMAAKRAwACnOo4VjyzYcbK44llIAQ")
      elif count == 130:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEN2DbUTBcuXuSGMwnSRrfHNqTsydoAAIYAwACSPtBVql7BPcv3fkmHgQ")
      elif count == 140:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEPGDbUVNU4sur49XQR21R5mDK2MTuAAJ8AgACEjpBVti8pBOmQ-GhHgQ")
      elif count == 150:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALASWDbNZTcEdbBZLDTWJUUyI28t8GFAAKDAQACW9YqGCcn5HlB2BFHIAQ")
      elif count == 160:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAXWDbNkZQifrUCZuiDVbgzVFUv3ZdAAIDAwACf7k5VsRb3FPkL5P2IAQ")
      elif count == 170:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEQWDbUYCTuDhxi8JW0uYZpGU2UcpBAAIqAwACVPs4VslBUME7PI2uHgQ")
      elif count == 180:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAALAX2DbNkfJxEL9LCFjlPnmP2wuQteHAAIuBAACS0k5Vi96vtzMVBELIAQ")
      elif count == 190:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIESmDbUZ2htsAZIkyDT6Ksv7cObAjCAAJTAgACkWRBVvyi4w2ai5amHgQ")
      elif count == 199:
                    await bot.send_sticker(chat_id,"CAACAgUAAxkBAAIEXGDbUf57NSGZOgAB4GVSKAJilDWwdAAC9AIAApBzQFbLWEHH8Pswhh4E")
      elif count == 200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAS2DbNZVlilesDRpcaTHL8xxE7vSLAAKFAQACW9YqGGcqtjuLAj1EIAQ")
      elif count == 225:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIElWDcD7_QjC1Kkbr2pjQzhShBuBNHAAKGAQACW9YqGCcHRNH2YHw9HgQ")
      elif count == 250:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIElmDcD9GOiYi4njwq7jmiXKWTaqVpAAKHAQACW9YqGLoAAcrvG_1fMh4E")
      elif count == 275:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEl2DcD-aHYyB1nhviKoJoi-oxUCbqAAKIAQACW9YqGBi4ekz9WZkBHgQ")
      elif count == 300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEmGDcD_pChuQF2YV_QYOqPLdirA3WAAKJAQACW9YqGBhkcSvmxCK0HgQ")
      elif count == 325:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEmWDcEAoVnn5n2x_iXqs52oRXg3p_AAKKAQACW9YqGB_kgD1Ax2LVHgQ")
      elif count == 350:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEmmDcEEASpD1mfNVv8OIQoo8IAAFx3gACiwEAAlvWKhjfJde0-fs_4B4E")
      elif count == 375:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEp2DcEHULRaejvUjWLN-Cncc-MB2PAAKMAQACW9YqGLdfWFF_dCi5HgQ")
      elif count == 400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEqGDcEIphJoIfydINtJDBiMosQFF4AAKNAQACW9YqGI1aSXP5ajN-HgQ")
      elif count == 425:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEqWDcEKy9rzG8LWMNHae3gogXw4RHAAKOAQACW9YqGJihagv76qx-HgQ")
      elif count == 450:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEqmDcEL-Sn-KPtQIQVOp7-INSAAEkyAACjwEAAlvWKhj-Xyo1z-wAASseBA")
      elif count == 475:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAj2DbOcy9R31WJyH6BxJj1Aq0DOH3AAKQAQACW9YqGJcbNF6RK3NUIAQ")
      elif count == 500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAkGDbOc3bdFb9rMO3uwEAAereBZR0pwACkQEAAlvWKhgDp1k6OPv46CAE")
      elif count == 525:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEuWDcEPNAs1rzmkV6Dp1KJ30Dp3VvAAKSAQACW9YqGAABnwkpjfnzdx4E")
      elif count == 550:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEumDcEQewwf7SVulbyyG3YKTO0v73AAKTAQACW9YqGFRVs6C6moCOHgQ")
      elif count == 575:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAq2DbOmb9FUwkATVDYAlhsFOmMcF5AAKUAQACW9YqGCvPzoMmogIiIAQ")
      elif count == 600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEv2DcES6kVUuE0-U9jSty2l3Y5zXUAAKVAQACW9YqGOgwXim4y0UyHgQ")
      elif count == 625:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEwGDcEUGNjB5TmELSqjjMb_wciIx-AAKWAQACW9YqGG_7RELWmJBFHgQ")
      elif count == 650:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEwWDcEVSShsHOAmPOR4sKJpp7Okn9AAKXAQACW9YqGMgDgKaXJAU0HgQ")
      elif count == 675:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEwmDcEWXxzJuRArktdLkMP2Ap7P0RAAKYAQACW9YqGGcuGWoEGTKVHgQ")
      elif count == 700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAsGDbOmmshfdpwmCSryBchmoK3yTxAAKZAQACW9YqGPTEWeDhdOVOIAQ")
      elif count == 725:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEy2DcEYQ5dFoqafo80zbxECffbalAAAKaAQACW9YqGEq6P7tuva8CHgQ")
      elif count == 750:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAsmDbOmrNDjq0yIr3eWCoIy91syzpAAKbAQACW9YqGOtGZWA98zCaIAQ")
      elif count == 775:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAs2DbOmsuO7u5AdPO9TPF1XW5n8rOAAKcAQACW9YqGFETXctTCf3dIAQ")
      elif count == 800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEzmDcEadN5kE_Su3tayEahBjUxWrNAAKdAQACW9YqGIBhBKzK4V0cHgQ")
      elif count == 825:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEz2DcEcsZ2VM6nky9OGCH5RjiSeiXAAKeAQACW9YqGJ33T4ayPCslHgQ")
      elif count == 850:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE0GDcEdwjArhgbjNw6zqg7Gf81qN4AAKfAQACW9YqGE_RowPqmchSHgQ")
      elif count == 875:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE0WDcEfTmXYb8LpifdN6trHmb3JuJAAKgAQACW9YqGFRfI6i6_yB5HgQ")
      elif count == 900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE0mDcEj9_kL_DAAGI_mCTbuIca2CcLQACoQEAAlvWKhjEOfieo8C4ox4E")
      elif count == 925:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE02DcElLl2QABSQ74nh9WKxowXjdwbwACogEAAlvWKhiEk4OOcjihuB4E")
      elif count == 950:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE1GDcEmRPod5gxQ7IgvAkG-nNK2tfAAKjAQACW9YqGB1ij6GWOAMMHgQ")
      elif count == 975:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAu2DbOnBUZ5DFwavvXo3Zq6hX5GrZAAKkAQACW9YqGGzROjV9WdVBIAQ")
      elif count == 1000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAvGDbOnFkRPePdhEWXBwTSV4eJfjTAAKlAQACW9YqGAluL79s0KEQIAQ")
      elif count == 1100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE5GDcEpc_TgE3d3jqO1j7O4ehyr23AAKmAQACW9YqGNmy9ZJmPsQUHgQ")
      elif count == 1200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA6WDbO1TxfZyF69PzmCw7nsrB2LDvAAKnAQACW9YqGEVp0JPc4nO6IAQ")
      elif count == 1300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE52DciNL-2hlKIz-225JCVozKD7SCAAKoAQACW9YqGLjrkXe6ArJJHgQ")
      elif count == 1400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA62DbO1YL1arJf9zVgdTGIVB7MUGhAAKpAQACW9YqGAWw3fw07KjYIAQ")
      elif count == 1500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6GDciT3DrSed3KGLqX1rVcPwU_xuAAKqAQACW9YqGN0Vs6wobkM7HgQ")
      elif count == 1600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA7WDbO1jGcxdqGAVsFhsXKoMp1epDAAKrAQACW9YqGLsCrwgNIGYkIAQ")
      elif count == 1700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6WDciVyqWjpKkMINJiKpYicFwXyOAAKsAQACW9YqGDw9w7xAMVc2HgQ")
      elif count == 1800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA72DbO1jWqU4PWKin9Bp9YEAZVnqQAAKtAQACW9YqGKEnAe3tZlvHIAQ")
      elif count == 1900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8GDbO1lPUheD5q2KRr1E0ue07bVGAAKuAQACW9YqGOq5CMnZqqvdIAQ")
      elif count == 2000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8WDbO1lSjFdU0zOJsCxglr41pTVOAAKvAQACW9YqGPFJNraaGLBkIAQ")
      elif count == 2100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6mDciXh6JuJ1QMSEXVksP0Fuw8oaAAKwAQACW9YqGFPovfk8HR_fHgQ")
      elif count == 2200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQmDbPPPsIgABUtrgFfZsu7GdAAEUxQYAArEBAAJb1ioYog7dqaYf2M0gBA")
      elif count == 2300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQ2DbPPRsp7QrM-wQBgHBb0SZzl13AAKyAQACW9YqGDH2xakhpikbIAQ")
      elif count == 2400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE62Dcimptq28z1ZRWDJg5oP513hdlAAKzAQACW9YqGEXNpSVgfaxQHgQ")
      elif count == 2500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE7GDcinzSnQ5zQ5cJ2qjrlvZZMQEbAAK0AQACW9YqGNfPUT-wLVZfHgQ")
      elif count == 2600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBRmDbPPXuU7h3tgaF1PEGHUtR4jp0AAK1AQACW9YqGIrf25Ws6cZgIAQ")
      elif count == 2700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE-2Dcir1OhXW6ogrw3uf_Nn6HO-GYAAK2AQACW9YqGEqRGCn0L8j0HgQ")
      elif count == 2800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_GDcis2We8LY2R89ICjDj1NyMauzAAK3AQACW9YqGGPdw7iHyjmZHgQ")
      elif count == 2900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_WDciu5e52XCAf_UzaZPvltnutPNAAK4AQACW9YqGPKt5abxW-lJHgQ")
      elif count == 3000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBOmDbPKJTEw96snijk3zWDju5o0cwAAK5AQACW9YqGNTV9iTuJqtXIAQ")
      elif count == 3100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_2DcixPJFDqIcErYXTxAy9PTdwwGAAK6AQACW9YqGO65_NqjiZU3HgQ")
      elif count == 3200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFAAFg3IskT3g2CtuSoI0hn4nqKxMB2QACuwEAAlvWKhho36LfXBFaIh4E")
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

