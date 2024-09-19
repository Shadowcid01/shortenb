
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import *
from helper_func import encode, get_message_id
import logging
from pyrogram import Client, filters
import aiohttp
import asyncio
from pyshorteners import Shortener


logging.basicConfig(filename='app.log', level=logging.DEBUG, encoding='utf-8')


@Client.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nThis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(
                text="Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nThis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n<blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup)

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(
                text="Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nThis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n<blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup)

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command('batch_plus'))
async def batch_plus(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(
                text="Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nThis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote=True)
            continue

    while True:
        try:
            num_files_message = await client.ask(
                text="Enter the number of files you want to batch process:",
                chat_id=message.from_user.id,
                filters=filters.text,
                timeout=60
            )
        except:
            return
        
        if num_files_message.text.isdigit():
            num_files = int(num_files_message.text)
            break
        else:
            await num_files_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)
            continue

    l_msg_id = f_msg_id + num_files - 1

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{l_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await num_files_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command('batch_pro'))
async def batch_pro(client: Client, message: Message):
    async def get_message(prompt, filter_type):
        while True:
            try:
                response = await client.ask(
                    text=prompt,
                    chat_id=message.from_user.id,
                    filters=filter_type,
                    timeout=60
                )
            except:
                return None
            
            msg_id = await get_message_id(client, response)
            if msg_id:
                return msg_id
            else:
                await response.reply("❌ Error\n\nThis post is not from the DB Channel or the link is invalid.", quote=True)

    # Step 1: Get the first message ID
    f_msg_id = await get_message(
        "Forward the First Message from DB Channel (with Quotes) or Send the DB Channel Post Link",
        filters.forwarded | (filters.text & ~filters.forwarded)
    )
    if not f_msg_id:
        return

    # Step 2: Get the total number of files
    while True:
        try:
            total_files_message = await client.ask(
                text="Enter the total number of files to process:",
                chat_id=message.from_user.id,
                filters=filters.text,
                timeout=60
            )
        except:
            return
        
        if total_files_message.text.isdigit():
            total_files = int(total_files_message.text)
            break
        else:
            await total_files_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)

    # Step 3: Get the last message ID
    l_msg_id = await get_message(
        "Forward the Last Message from DB Channel (with Quotes) or Send the DB Channel Post link",
        filters.forwarded | (filters.text & ~filters.forwarded)
    )
    if not l_msg_id:
        return

    # Step 4: Get the number of files per batch
    while True:
        try:
            batch_size_message = await client.ask(
                text="Enter the number of files per batch:",
                chat_id=message.from_user.id,
                filters=filters.text,
                timeout=60
            )
        except:
            return
        
        if batch_size_message.text.isdigit():
            batch_size = int(batch_size_message.text)
            break
        else:
            await batch_size_message.reply("❌ Error\n\nPlease enter a valid number.", quote=True)

    # Step 5: Notify user that batching is in progress
    batching_msg = await message.reply_text("📦 Batching in progress, please wait...")

    # Calculate the number of batches and generate links
    num_batches = (total_files + batch_size - 1) // batch_size
    batch_links = []

    for i in range(num_batches):
        start_id = f_msg_id + i * batch_size
        end_id = min(f_msg_id + (i + 1) * batch_size - 1, l_msg_id)
        batch_string = f"get-{start_id * abs(client.db_channel.id)}-{end_id * abs(client.db_channel.id)}"
        base64_string = await encode(batch_string)
        link = f"https://telegram.me/{client.username}?start={base64_string}"
        batch_links.append(link)

    # Step 6: Prepare the final message with all batch links in groups of 10
    MAX_LINKS_PER_MESSAGE = 10
    link_chunks = [batch_links[i:i + MAX_LINKS_PER_MESSAGE] for i in range(0, len(batch_links), MAX_LINKS_PER_MESSAGE)]

    for chunk_idx, link_chunk in enumerate(link_chunks):
        # Prepare the message text for this chunk
        message_text = f"<b>Batch_pro links ({chunk_idx + 1}/{len(link_chunks)}):</b>\n\n" + "\n".join(
            [f"Batch Link {i + 1}\n{link}" for i, link in enumerate(link_chunk)]
        )
        await message.reply_text(message_text, parse_mode="HTML")

    await batching_msg.edit("✅ Batching complete!")



# Ensure these are set correctly in config.py
SHORTENER_API = os.environ.get("SHORTENER_API", "0aef028290a85e9346edab753a4d557a7458d6e4")
SHORTENER_WEBSITE = os.environ.get("SHORTENER_WEBSITE", "https://urlshortx.io")
SHORTENER_API2 = os.environ.get("SHORTENER_API2", "d86f57a6ae444bdc63318e7b111a02b8edb8a59a")
SHORTENER_WEBSITE2 = os.environ.get("SHORTENER_WEBSITE2", "https://linkshortx.in")

# Define delay to avoid blocking
DELAY = 2

# Function to shorten links using specified API and URL
async def shorten_link(url, api_key, api_url):
    params = {'api': api_key, 'url': url}
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

@Client.on_message(filters.private & filters.command('shortlink1'))
async def shortlink1(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: <code> /shortlink1 https://linkshortx.in</code>")
    
    original_url = message.text.split(maxsplit=1)[1]
    processing_msg = await message.reply_text("♻️ Processing your link, please wait...")
    
    try:
        # Shorten link using the first shortener
        short_url1 = await shorten_link(original_url, SHORTENER_API, f"{SHORTENER_WEBSITE}/api")
        await asyncio.sleep(DELAY)
        await processing_msg.delete()
        await message.reply_text(f"Your shortened link:\n\n<code>{short_url1}</code>")
    except Exception as e:
        await processing_msg.delete()
        await message.reply_text(f"Error occurred: {e}")

@Client.on_message(filters.private & filters.command('shortlink2'))
async def shortlink2(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /shortlink2 <code> /shortlink1 https://linkshortx.in</code>")
    
    original_url = message.text.split(maxsplit=1)[1]
    processing_msg = await message.reply_text("♻️ Processing your link, please wait...")
    
    try:
        # Shorten link using the second shortener
        short_url2 = await shorten_link(original_url, SHORTENER_API2, f"{SHORTENER_WEBSITE2}/api")
        await asyncio.sleep(DELAY)
        await processing_msg.delete()
        await message.reply_text(f"Your shortened link:\n\n<code>{short_url2}</code>")
    except Exception as e:
        await processing_msg.delete()
        await message.reply_text(f"Error occurred: {e}")

@Client.on_message(filters.private & filters.command('shortlink'))
async def shortlink(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /shortlink <link>")
    
    original_url = message.text.split(maxsplit=1)[1]
    processing_msg = await message.reply_text("♻️ Processing your links, please wait...")
    
    try:
        # Shorten link using both shorteners
        short_url1 = await shorten_link(original_url, SHORTENER_API, f"{SHORTENER_WEBSITE}/api")
        await asyncio.sleep(DELAY)
        short_url2 = await shorten_link(original_url, SHORTENER_API2, f"{SHORTENER_WEBSITE2}/api")
        await processing_msg.delete()
        await message.reply_text(f"Your shortened links:\n\n<code>Shortener 1: {short_url1}\nShortener 2: {short_url2}</code>")
    except Exception as e:
        await processing_msg.delete()
        await message.reply_text(f"Error occurred: {e}")

