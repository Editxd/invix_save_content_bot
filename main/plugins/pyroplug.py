import asyncio
import time
import os
import logging
from pyrogram.enums import ParseMode, MessageMediaType
from .. import Bot, bot
from main.plugins.progress import progress_for_pyrogram
from main.plugins.helpers import screenshot
from pyrogram import Client, filters
from pyrogram.errors import ChannelBanned, ChannelInvalid, ChannelPrivate, ChatIdInvalid, ChatInvalid, FloodWait
from main.plugins.helpers import video_metadata
from telethon import events

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ... (other imports and code)

async def check(userbot, client, link):
    logging.info(link)
    msg_id = 0
    try:
        msg_id = int(link.split("/")[-1])
    except ValueError:
        if '?single' not in link:
            return False, "**Invalid Link!**"
        link_ = link.split("?single")[0]
        msg_id = int(link_.split("/")[-1])
    if 't.me/c/' in link:
        try:
            chat = int('-100' + str(link.split("/")[-2]))
            await userbot.get_messages(chat, msg_id)
            return True, None
        except ValueError:
            return False, "**Invalid Link!**"
        except Exception as e:
            logging.info(e)
            return False, "Have you joined the channel?"
    else:
        try:
            chat = str(link.split("/")[-2])
            await client.get_messages(chat, msg_id)
            return True, None
        except Exception as e:
            logging.info(e)
            return False, "Maybe bot is banned from the chat, or your link is invalid!"

# ... (other functions and code)

async def get_bulk_msg(userbot, client, sender, msg_link, i):
    x = await client.send_message(sender, "Processing!")
    file_name = ''
    # Check if messages can be retrieved from the link
    result, error_message = await check(userbot, client, msg_link)

    if result:
        await get_msg(userbot, client, sender, x.id, msg_link, i, file_name)
    else:
        await client.edit_message_text(sender, x.id, f"Error: {error_message}")

# ... (other code)

async def main():
    # ... (other setup code)

    # Example usage of get_bulk_msg function
    link_to_process = "https://t.me/c/1880328213/4413/4451"
    i_to_process = 123  # Replace with the actual message ID you want to process
    await get_bulk_msg(userbot_instance, client_instance, sender, link_to_process, i_to_process)

    # ... (other code)

if __name__ == "__main__":
    asyncio.run(main())
