#ТЕЛЕГРАМ БОТ

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bots_commands import *

app = ApplicationBuilder().token("5521249095:AAFifgGXf9Ut8tv5lUMMZzb_KoxKa9g5x_c").build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()