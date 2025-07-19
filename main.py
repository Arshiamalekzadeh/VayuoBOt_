from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import os

# تنظیمات اولیه
BOT_TOKEN = os.getenv("BOT_TOKEN")
DESTINATION_CHANNEL = -1002659890273  # شناسه کانال

# اگر متغیر محیطی تنظیم شده باشد، از آن استفاده کنید
dest_channel_str = os.getenv("DEST_CHANNEL")
if dest_channel_str:
    DESTINATION_CHANNEL = int(dest_channel_str)

bot = Bot(token=BOT_TOKEN)

# تابعی برای ارسال پیام به کانال در زمان استارت بات
def start(update, context):
    bot.send_message(chat_id=DESTINATION_CHANNEL, text="🔹 دلامممممممممممممممممممممممممم")

# هندلر برای دریافت فایل‌ها و ارسال به کانال
def handle_file(update, context):
    message = update.message
    file = None
    if message.audio:
        file = message.audio.file_id
        bot.send_audio(chat_id=DESTINATION_CHANNEL, audio=file, caption="")
    elif message.video:
        file = message.video.file_id
        bot.send_video(chat_id=DESTINATION_CHANNEL, video=file, caption="")
    elif message.document:
        file = message.document.file_id
        bot.send_document(chat_id=DESTINATION_CHANNEL, document=file, caption="")
    elif message.photo:
        file = message.photo[-1].file_id  # آخرین عکس به عنوان فایل انتخاب می‌شود
        bot.send_photo(chat_id=DESTINATION_CHANNEL, photo=file, caption="")

    message.reply_text("✅ فایل بدون کپشن به کانال ارسال شد.")

# راه‌اندازی بات
def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.audio | Filters.video | Filters.document | Filters.photo, handle_file))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()