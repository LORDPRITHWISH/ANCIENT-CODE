from telegram import Update
from telegram.ext import *
import logging
import emoji
import time
import random

smiley = "\U0001F600"



def unemo(text):
    return emoji.replace_emoji(text,'')

print('Starting bot ...')

def error_handler(update: Update, context: CallbackContext, error: Exception, error_message: str):
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=f"An error occurred: {error_message}")
    logger.error(f'Update {update} caused error {error}: {error_message}')




async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mes=str(unemo(update.message.text))
    await update.message.reply_text(getreply(mes))
    
def getreply(mess) :
    
    mess='chat processing in development so your text in reverse is'+mess[::-1]
    return mess
    
async def junkie(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # mes=update.message.text.split()[0]
    mes=update.message.text
    # k=mes,
    # print(k)
    await update.message.reply_text(f' YOU WROTE {mes} and the command dosent exist {smiley}')
   
async def timesay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    await update.message.reply_text(f"it is {time.ctime()}")
    
async def comboy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    com=str(unemo(update.message.text)).strip().lower()[1:]
    res=comres(com)
    await update.message.reply_text(res)
            
def comres(x) :
    match x:
        case 'help' :
            return('TRY WRITIG SOMETHING AS YOUR HEART DESIRES REALLY ANYTHING \n AND I WILL RESPOND TO IT')        
        case 'praise' :
            op=['Your face just makes my day','Your skills are so so wonderous','ALL HAIL THE KING !']
            return random.choice(op)
        case 'insult' :
            op=['WTF cow','You sick fuck','you are a useless piece of shit','death to you, dam it']
            return random.choice(op)
        
            
async def tagit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('HEYO COOL MAN')
    await update.message.reply_text(text="good",)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    # await update.message.reply_sticker(sticker='C:\\Users\\prithis\\Desktop\\py storage\\png-transparent-airplane-drawing-spacecraft-rocket-cartoon-outer-space-aircraft-military-aircraft-vehicle.png')

    
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("WELCOME TO THE LAND OF THE MOST CRAZYEST BOT \n THE DARK BOT  made by LORDPRITHWISH")



app = ApplicationBuilder().token('6064075063:AAFRsbJHDO_I8ee8ieG_q3PPpKSUJ_FwgiI').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("time", timesay))
app.add_handler(CommandHandler(['help','praise','insult'],comboy))
app.add_handler(MessageHandler(filters.COMMAND,junkie))
# app.add_handler(MessageHandler(filters.CAPTION, tagit))
app.add_handler(MessageHandler(filters.TEXT,reply))
app.add_error_handler(error_handler)

app.run_polling()
