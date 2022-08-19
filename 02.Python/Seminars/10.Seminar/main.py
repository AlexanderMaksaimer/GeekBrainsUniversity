from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import os
from random import randint, choice

token = os.getenv('TOKEN')
updater = Updater(token)
dispatcher = updater.dispatcher

candy_count = 300
max_candy_takes = 28
PLAYER, MOVE = range(2)
player_1 = ''
player_2 = 'Сладкоежка'
current_player = None

print('Бот работает...')


def start(update, context):
    global candy_count
    candy_count = 300  # обновляем начальное количество, если пользователь выбрал "играть снова"
    arg = context.args
    if not arg:
        #  приветствие
        context.bot.send_message(update.effective_chat.id,
                                 f"Привет! Меня зовут {player_2}. Давай сыграем с тобой в игру!\n"
                                 f"У меня есть {candy_count} конфет,"
                                 f" за один ход НУЖНО взять от 1 до {max_candy_takes}\n"
                                 f"Кто делает последний ход - тот выиграл")
        # отправляем стикер
        context.bot.send_sticker(update.effective_chat.id,
                                 'CAACAgIAAxkBAAEFjNJi94K3z0gnfHFSLvxLxQ22fzSCKQACpxEAAgK7gUk-x3dwqdO83CkE')
    context.bot.send_message(update.effective_chat.id, 'Представься, пожалуйста!')
    return PLAYER


def player_name(update, context):
    """
    Получаем имя игрока, начинаем игру
    """
    global player_1, player_2, current_player
    player_1 = update.message.text
    current_player = choice([player_1, player_2])  # Выбор кто ходит первым
    context.bot.send_message(update.effective_chat.id, f'Первым ходит {current_player}')
    if current_player == player_2:
        bot_move(update, context)  # передача хода боту
    else:
        context.bot.send_message(update.effective_chat.id, 'Сколько конфет возьмёте?')  # вопрос игроку
    return MOVE


def take_move(update, context):  # ход игрока
    global candy_count, current_player
    try:  # проверка на ввод пользователем числа и разрешенного количества конфет
        take_candies = int(update.message.text)
        if 1 <= take_candies <= max_candy_takes:
            candy_count -= take_candies
        else:
            context.bot.send_message(update.effective_chat.id,
                                     f'За раз можно взять от 1 до {max_candy_takes} конфет')
            return MOVE
    except:
        context.bot.send_message(update.effective_chat.id, f'Введите число от 1 до 28')
        return MOVE
    context.bot.send_message(update.effective_chat.id, f'На столе осталось {candy_count} конфет...')
    if candy_count <= max_candy_takes:  # Проверка выигрыша бота
        context.bot.send_message(update.effective_chat.id,
                                 f'{player_2} забрал последние {candy_count} конфет и победил!')
        return ConversationHandler.END
    bot_move(update, context)  # передача хода боту


def bot_move(update, context):  # ход бота
    global candy_count, current_player
    take_candies = randint(1, max_candy_takes)
    candy_count -= take_candies
    context.bot.send_message(update.effective_chat.id, f'{player_2} берёт {take_candies} конфет')
    if candy_count <= max_candy_takes:  # Проверка выигрыша игрока
        context.bot.send_message(update.effective_chat.id,
                                 f'{player_1} забрал последние {candy_count} конфет и победил!')
        return ConversationHandler.END
    else:  # передача хода игроку
        context.bot.send_message(update.effective_chat.id, f'На столе осталось {candy_count} конфет...')
        context.bot.send_message(update.effective_chat.id, 'Сколько конфет возьмёте?')
        return MOVE


def stop(update, context):  # конец игры
    context.bot.send_message(update.effective_chat.id, 'Игра окончена!')
    return ConversationHandler.END


def unknown_command(update, context):  # обработчик неизвестных команд и/или сообщений
    context.bot.send_message(update.effective_chat.id, f'Я умею только в конфеты играть...')
    context.bot.send_sticker(update.effective_chat.id,
                             'CAACAgIAAxkBAAEFjOxi94xmrJiRNQooduKh4GR4in4fCQAC7BUAAukAARhItE_tlWzTa_gpBA')
    context.bot.send_message(update.effective_chat.id, f'Хочешь сыграть ещё - введи /start')


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        PLAYER: [MessageHandler(Filters.text, player_name)],
        MOVE: [MessageHandler(Filters.text, take_move)]},
    fallbacks=[CommandHandler('stop', stop)])
message_handler = MessageHandler(Filters.text, unknown_command)
unknown_handler = MessageHandler(Filters.command, unknown_command)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()