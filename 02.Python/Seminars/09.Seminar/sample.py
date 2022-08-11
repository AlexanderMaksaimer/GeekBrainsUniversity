from itertools import count
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from functions import *

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start) #/start
info_handler = CommandHandler('info', info) #/info
add_handler = CommandHandler('add',plus) #/add
message_handler = MessageHandler(Filters.text, message)
#calculation_handler = MessageHandler(Filters.text,calculation)
unknown_handler = MessageHandler(Filters.command, unknown) #/game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)
#dispatcher.add_handler(calculation_handler)

print('server started')
updater.start_polling()
updater.idle()