from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""[!](https://te.legra.ph/file/7ab7d5a4ca9aadfef8943.jpg)Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},

ᴍʏ ꜰᴇᴀᴛᴜʀᴇꜱ :

★ ᴇᴀꜱʏ ᴛᴏ ᴀᴄᴄᴇꜱꜱ 
★ ɴᴏ ᴅᴏᴡɴᴛɪᴍᴇ
★ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴʏ ᴠᴇʀꜱɪᴏɴ ᴏꜰ ꜱᴇꜱꜱɪᴏɴ
★ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ɢᴇɴʀᴇᴀᴛᴇ ᴛʜᴇ  ꜱᴇꜱꜱɪᴏɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ

Mᴀᴅᴇ ᴡɪᴛʜ  : [✶ ᴛᴇᴀᴍ ᴠᴀᴍᴘɪʀᴇ ɴᴇᴛᴡᴏʀᴋ ✶](https://t.me/TEAM_VAMPIR) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(text="🪄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🪄", callback_data="generate"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
