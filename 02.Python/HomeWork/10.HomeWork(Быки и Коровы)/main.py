from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import os
from controller import *
from config import TOKEN
import logging

 # Включим ведение журнала
logging.basicConfig(
     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
 )
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

guess = None
PLAYER, STEP = 0, 1
player = None

print('Погнали')

def start(update, context):
    global num, count
    num = create_number()  # "загадываем" число
    count = 1
    context.bot.send_message(update.effective_chat.id,
                             f'Bongiorno!! Имеешь желание катнуть в "Быки и Коровы"?\n')
    context.bot.send_message(update.effective_chat.id,
                             f'Для выхода из игры введите /stop\n')
    context.bot.send_message(update.effective_chat.id, 'Меня зовут Владыка Ситхов и Быков, а как тебя величают?')
    return PLAYER


def player_name(update, context):
    global player, count
    player = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Игра началась... <b>У тебя есть 10 попыток...</b>')
    context.bot.send_message(update.effective_chat.id, 'Введите число:')
    context.bot.send_message(update.effective_chat.id, f'Попытка №{count}...')
    return STEP


def take_move(update, context):
    global guess, count
    try:
        guess = int(update.message.text)
    except:
        context.bot.send_message(update.effective_chat.id, f'Введите число:')
        return STEP
    if not search_dupli(guess):
        context.bot.send_message(update.effective_chat.id, f'В загаданном числе цифры не повторяются')
        return STEP
    if guess < 1000 or guess > 9999:
        context.bot.send_message(update.effective_chat.id, f'Загаданное число состоит из 4 цифр')
        return STEP
    count += 1  # увеличиваем счетчик попыток !!! обязательно после проверок ввода
    bull_cow = bulls_and_cows(num, guess)
    if bull_cow[0] == 4:  # если быков 4 - выигрыш
        context.bot.send_message(update.effective_chat.id,
                                 f'Да ты просто Ванга, {player}! Смог отгадать число: {num} за {count - 1} попыток')
        return ConversationHandler.END
    if count <= 10:  # используем попытки
        context.bot.send_message(update.effective_chat.id, f'быков - {bull_cow[0]} | коров - {bull_cow[1]}')
        context.bot.send_message(update.effective_chat.id, f'Попытка № {count}:')
        return STEP
    else:  # если попыток больше 10 - проигрыш
        context.bot.send_message(update.effective_chat.id,
                                 f'Сожалею, {player}, однако ты использовал все свои {count - 1} попыток и слил катку')
        return ConversationHandler.END

def another_message(update, context):  # случаи ввода иных сообщений
    context.bot.send_message(update.effective_chat.id, f'Мы тут играем только в Быки и Коровы')
    context.bot.send_message(update.effective_chat.id, f'Если хочешь сыграть ещё раз - введи /start')


def stop(update, context):  # конец игры
    user = update.message.from_user
#      # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s завершил разговор.", user.first_name)
#      # Отвечаем на отказ поговорить
    context.bot.send_message(update.effective_chat.id, 
        'Мое дело предложить - Ваше отказаться'
        'Che la forza sia con voi!')
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        PLAYER: [MessageHandler(Filters.text, player_name)],
        STEP: [MessageHandler(Filters.text, take_move)]
    },
    fallbacks=[CommandHandler('stop', stop)])

message_handler = MessageHandler(Filters.text, another_message)
unknown_handler = MessageHandler(Filters.command, another_message)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)

dispatcher.add_handler(conv_handler)

print('Чувствую силу в тебе')
updater.start_polling()
updater.idle()
