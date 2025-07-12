from pyrogram import Client, filters
from pyrogram.types import Message
import os

api_id = 1137903
api_hash = "6007f2a379420aa71e6ad8de2aa32c299b947017429868ca01c20fe2cf3ce5ce"
bot_token = os.getenv("BOT_TOKEN")

dest_channel_str = os.getenv("DEST_CHANNEL")
if not dest_channel_str:
    raise ValueError("Environment variable DEST_CHANNEL is not set.")
destination_channel = int(dest_channel_str)

app = Client("vayuo_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.private & (filters.audio | filters.video | filters.document | filters.photo))
async def handle_file(client, message: Message):
    file = None
    if message.audio:
        file = message.audio.file_id
        await client.send_audio(destination_channel, file, caption="")
    elif message.video:
        file = message.video.file_id
        await client.send_video(destination_channel, file, caption="")
    elif message.document:
        file = message.document.file_id
        await client.send_document(destination_channel, file, caption="")
    elif message.photo:
        file = message.photo.file_id
        await client.send_photo(destination_channel, file, caption="")

    await message.reply("✅ فایل بدون کپشن به کانال ارسال شد.")

app.run()
