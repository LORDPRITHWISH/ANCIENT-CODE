import logging
from telegram.ext import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a function to handle incoming messages and captions
def echo(update, context):
    text = update.message.text or update.message.caption
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# Create a bot and register the message and caption handler
updater = updater(token='6064075063:AAFRsbJHDO_I8ee8ieG_q3PPpKSUJ_FwgiI', use_context=True)
dispatcher = updater.dispatcher
echo_handler = MessageHandler(filters.text & (~filters.command), echo)
caption_handler = MessageHandler(filters.caption & (~filters.command), echo)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caption_handler)

# Start the bot
updater.start_polling()
