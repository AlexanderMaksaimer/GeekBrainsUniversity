#1)Добавить функцию add, которая примет два числа и сложит их

from ntpath import join


def plus(update, context):
    arg = context.args
    print(arg) 
    if not arg:#что будет если не ввели аргументов 
        context.bot.send_message(update.effective_chat.id, "Забыли ввести аргументы")
    try:
        arg = list(map(int,arg))
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Вы ввели не число")
    res = sum(arg)
    arg = "+".join(list(map(str,arg)))
    context.bot.send_message(update.effective_chat.id, f"{arg} = {res}") #возвращаем в чате введенные аргументы и результат сложения 

# def calculation(update,context):
#     number_1 = update.message.text
#     try:
#         eval(number_1)
#         context.bot.send_message(update.effective_chat_id,f"{number_1} = {eval(number_1)}")
#     except:
#         context.bot.send_message(update.effective_chat_id,f"Введите выражение для рассчета. Например: 1+2(3*4)*6")
    
def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "I'am Batman")


def message(update, context):
    text = update.message.text
    try:
        eval(text)
        context.bot.send_message(update.effective_chat.id, f"{text} = {eval(text)}")
        #context.bot.send_message(update.effective_chat_id,f"{text} = {eval(text)}")
    except:
        if text.lower() == 'привет':
            context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
        else:
            context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')
