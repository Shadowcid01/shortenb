#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Owner : <a href='tg://user?id={OWNER_ID}'>Luffy</a>\n○ My Channel : <a href='https://t.me/POCKET_PFM'>Pocket PFM/a>\no Issues: <a href='https://t.me/PFM_SUPPORT_BOT'></a>\n○ Our Community : <a href='https://t.me/Audio_Versee'>Community</a>\n○ ᴄʜᴀᴛ : <a href='https://t.me/+r-6ztnSy3yo3Mzc9'>PFM</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/PFM_SUPPORT_BOT')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
