from audioop import add
from itertools import count
import json
from telegram import Update, Bot
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from config import TOKEN
from functions import *

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

TITLE, TASK = range(2)

one_task = {
    'title':None,
    'description':None
}

def add_title(update,context):
    global one_task
    text = update.message.text
    if abs(len(text)) > 30:
        context.bot.send_message(
            update.effective_chat.id, f'Слишком длинный заголовок')
        return 
    one_task['title'] = text
    add_to_temp_file(text)
    context.bot.send_message(
        update.effective_chat.id, f'Обновлен заголовок. Сейчас словарь выглядит так: {one_task}')
    return TASK

def add_task(update,context):
    global one_task
    text = update.message.text
    if abs(len(text)) > 50:
        context.bot.send_message(
            update.effective_chat.id, f'Слишком длинный текст задачи')
    one_task['description'] = text
    add_to_temp_file(text)
    context.bot.send_message(
        update.effective_chat.id, f'Обновлена задача. Сейчас словарь выглядит так: {one_task}')
    task = dict(zip(['title','desciption'],[]))
    write_to_database(one_task)
    context.bot.send_message(
        update.effective_chat.id, f'Задача добавлена в базу данных')
    return ConversationHandler.END

def exit_add(update,context):
    context.bot.send_message(
        update.effective_chat.id, f'Операция прервана')
    return ConverssationHandler.END

def database_read():
    with open('data_file.json','', encoding='utf-8') as read_file:
        data_from_file = json.load(read_file,object_hook=_decode)
    return data_from_file

def write_to_database(task:Dict):
    database = database_read()
    id = len(database)+1
    database.update({id:task})
    with open('data_file.json','w',encoding='utf-8') as write_file:
        json.dump(database,write_file,#запись в файл
                ensure_ascii=False,#Для русского языка
                indent = 4)

def add_to_temp_file(string:str):
    with open('temp.txt','a',encoding='utf-8') as file:
        file.write(f'{string}\d')

def clear_temp_file():
    with open('temp.txt', 'w', encoding='utf-8') as file:
        file.write('')



start_handler = CommandHandler('start', start) #/start
info_handler = CommandHandler('info', info) #/info
add_handler = CommandHandler('add',plus) #/add
message_handler = MessageHandler(Filters.text, message)
conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('add', add)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            TITLE: [MessageHandler(Filters.text,add_title),CommandHandler('no',exit_add)],
            TASK: [MessageHandler(Filters.text, add_task), CommandHandler('no',exit_add)],
            
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('no', exit_add)],
    )

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