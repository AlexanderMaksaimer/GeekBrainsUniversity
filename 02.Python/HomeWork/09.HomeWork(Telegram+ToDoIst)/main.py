from telegram import Bot, Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import *
import os
import logging
from controller import *

 # Включим ведение журнала
logging.basicConfig(
     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
 )
logger = logging.getLogger(__name__)

ID = 'ID'
TASK = 'TASK'
STATUS = 'performed'
temp_task = None
temp_id = None
#кнопки
keyboard = ReplyKeyboardMarkup([
    [KeyboardButton('Глянуть все задачи'),
     KeyboardButton('Оценить на сколько ты хорош'),
     KeyboardButton('Оценить фронт работы')],

    [KeyboardButton('Добавить'),
     KeyboardButton('Изменить'),
     KeyboardButton('Удалить')],

    [KeyboardButton('Сохранить изменения'),
     KeyboardButton('Выход')]
], resize_keyboard=True)

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Bongiorno!", reply_markup=keyboard)
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Желаешь упорядочить свою жизнь, и ничего не забыть сделать сегодня/завтра или через год?")

def task_add(update, context):
    update.message.reply_text(add_task(data_base_tasks, update.message.text))
    return ConversationHandler.END

def change_id(update, _):
    update.message.reply_text('Введите ID задачи, которую вы хотите изменить:')
    return ID
    
def change_task(update, _):
    global temp_id
    temp_id = int(update.message.text)
    update.message.reply_text('Внесите желаемые изменения в задачу:')
    return TASK

def status_change(update, _):
    global temp_task
    temp_task = update.message.text
    update.message.reply_text('Введите статус задачи: 1 - выполнено, 0 - не выполнено')
    return STATUS

def change_task_status(update, context):
    temp_flag = update.message.text
    for k, v in data_base_tasks.items():
        if temp_id == k:
            v['TASK'] = temp_task
            v['performed'] = temp_flag
    update.message.reply_text('Задача изменена')
    return ConversationHandler.END

def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И куда тебя это привело?Снова ко мне...')
    elif text.lower() == 'глянуть все задачи':
        context.bot.send_message(update.effective_chat.id, f'{task_print(data_base_tasks, 1)}')
    elif text.lower() == 'оценить на сколько ты хорош':
        context.bot.send_message(update.effective_chat.id, f'{task_print(data_base_tasks, 2)}')
    elif text.lower() == 'оценить фронт работы':
        context.bot.send_message(update.effective_chat.id, f'{task_print(data_base_tasks, 3)}')
    elif text.lower() == 'добавить':
        context.bot.send_message(update.effective_chat.id, 'Напишите задачу, которую хотите добавить:')
        return TASK
    elif text.lower() == 'изменить':
        context.bot.send_message(update.effective_chat.id, f'{task_print(data_base_tasks, 1)}')
    elif text.lower() == 'сохранить изменения':
        context.bot.send_message(update.effective_chat.id, f'{info_save(data_base_tasks)}')
    elif text.lower() == 'удалить':
        context.bot.send_message(update.effective_chat.id, f'{task_print(data_base_tasks, 1)}')
        context.bot.send_message(update.effective_chat.id, 'Напишите номер (ID) задачи для последующего удаления:')
        return ID
    else:
        context.bot.send_message(update.effective_chat.id, f'Чепуху несешь')
    return update.message.text

def add(update, _):
    update.message.reply_text('Какую задачу хотите добавить?')
    return TASK

def mes_del(update, _):
    update.message.reply_text('Номер (ID) задачи, которую желаете удалить:')
    return ID

def delete_task(update, context):
    update.message.reply_text(del_task(data_base_tasks, update.message.text))
    return ConversationHandler.END

def cancel(update, _):
    #отмена действия
    update.message.reply_text('Сдаешь назад. Так не пойдет.')
    return ConversationHandler.END

def stop(update, _):
     # определяем пользователя
    user = update.message.from_user
     # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s завершил разговор.", user.first_name)
     # Отвечаем на отказ поговорить
    update.message.reply_text(
         'Мое дело предложить - Ваше отказаться'
         'Che la forza sia con voi!', 
        reply_markup=ReplyKeyboardRemove()
    )
     # Заканчиваем разговор.
    return ConversationHandler.END

def unknown(update, context):
        #Ответ на не распознанное сообщение
    context.bot.send_message(update.effective_chat.id, f'Иди порепетируй, а потом возвращайся')


     # Определяем обработчик разговоров `ConversationHandler` 
conv_handler = ConversationHandler(
        # точка входа в разговор
    entry_points=[MessageHandler(Filters.regex('^(Добавить)$'), add)],
        # этапы разговора
    states={
        TASK: [MessageHandler(Filters.text, task_add)]
    },
        # точка выхода из разговора
    fallbacks=[CommandHandler('stop', stop)]
    )
     # Определяем обработчик разговоров `ConversationHandler` 
conv_handler2 = ConversationHandler(
        # точка входа в разговор
    entry_points=[MessageHandler(Filters.regex('^(Удалить)$'), mes_del)],
        # этапы разговора
    states={
        ID: [MessageHandler(Filters.text, delete_task)]
    },
    # точка выхода из разговора
    fallbacks=[CommandHandler('stop', stop)]
    )
     # Определяем обработчик разговоров `ConversationHandler` 
conv_handler3 = ConversationHandler(
    # точка входа в разговор
    entry_points=[MessageHandler(Filters.regex('^(Изменить)$'), change_id)],
        # этапы разговора
    states={
        ID: [MessageHandler(Filters.text, change_task)],
        TASK: [MessageHandler(Filters.text, status_change)],
        STATUS: [MessageHandler(Filters.text, change_task_status)]
    },
        # точка выхода из разговора
    fallbacks=[CommandHandler('stop', stop)]
    )
    
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
stop_handler = CommandHandler('stop', stop)
new_rask_handler = CommandHandler('add', add)
enter_task_handler = CommandHandler('task_add', task_add)
cancel_handler = CommandHandler('cancel', cancel)
delete_task_handler = CommandHandler('mes_del', mes_del)
delete_task_id_handler = CommandHandler('delete_task', delete_task)
edit_id_handler = CommandHandler('change_id', change_id)
enter_edit_task_handler = CommandHandler('change_task', change_task)
edit_f_handler = CommandHandler('change_task_status', change_task_status)
edit_t_handler = CommandHandler('status_change', status_change)

message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown)  # /game

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(new_rask_handler)
dispatcher.add_handler(enter_task_handler)
dispatcher.add_handler(conv_handler2)
dispatcher.add_handler(conv_handler3)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(delete_task_handler)
dispatcher.add_handler(delete_task_id_handler)
dispatcher.add_handler(edit_id_handler)
dispatcher.add_handler(enter_edit_task_handler)
dispatcher.add_handler(edit_f_handler)
dispatcher.add_handler(edit_t_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)
    
print('Чувствую силу в тебе')
updater.start_polling()
updater.idle()
