#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS, LINKSHORTX_API
from helper_func import encode, get_message_id
from pyshorteners import Shortener
import aiohttp


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    s = Shortener()
    url = s.dagd.short(link)
    #Add Linkshortx link shortner
    api_url = "https://linkshortx.in/api"
    params={'api': LINKSHORTX_API,'url': link}
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url,params=params,raise_for_status=True) as response:
            data=await response.json()
            url2 =data["shortenedUrl"]

    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔁 Modern_Link_Share", url=f'https://telegram.me/share/url?url={url}')]
        ]
        )

    await second_message.reply_text(f"<b>Here is your link</b>\n\nNormal_Link: <code>{link}</code>\n\nModern_Link: <code>{url}</code>\n\nLinkshortX: <code>{url2}</code>", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"

    s = Shortener()
    url = s.dagd.short(link)
    #Add Linkshortx link shortner
    api_url = "https://linkshortx.in/api"
    params={'api': LINKSHORTX_API,'url': link}
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url,params=params,raise_for_status=True) as response:
            data=await response.json()
            url2 =data["shortenedUrl"]

    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔁 Modern_Link_Share", url=f'https://telegram.me/share/url?url={url}')]
        ]
        )

    await  channel_message.reply_text(f"<b>Here is your link</b>\n\nNormal_Link: <code>{link}</code>\n\nModern_Link: <code>{url}</code>\n\nLinkshortX: <code>{url2}</code>",  reply_markup=reply_markup)

