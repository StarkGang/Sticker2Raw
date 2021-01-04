from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from Configs import Config
import math
import os
from io import BytesIO
from PIL import Image

from loggers import logging

bot = TelegramClient("bot", api_id=Config.API_ID, api_hash=Config.API_HASH)
ToolsHD = bot.start(bot_token=Config.BOT_TOKEN)
sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
 
@ToolsHD.on(events.InlineQuery)
async def inline_handler(event):
    results = []
    query = event.text
    chat = -1001227729243
    async for lul in ToolsHD.iter_messages(chat, search=query, limit=20):
        results.append(
                await event.builder.photo(
                    file='https://png.pngtree.com/element_our/20190530/ourlarge/pngtree-search-icon-image_1257308.jpg',
                    text=lul.message,
                )
        )
    await event.answer(results)
                   
print("Bot Is Alive.")


def startbot():
    ToolsHD.run_until_disconnected()


if __name__ == "__main__":
    startbot()
