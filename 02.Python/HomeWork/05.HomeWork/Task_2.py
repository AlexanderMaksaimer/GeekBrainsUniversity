# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import functions as FUNC
import random

def game_players(num_of_players=2,candy_ammount=2021,aloud_ammount_on_turn=28):
    """Игра - где каждый игрок по очереди берёт доступное кол-во конфет
    Args:
        num_of_players (int, optional): Кол-во игроков Defaults to 2.
        candy_ammount (int, optional): Всего конфет. Defaults to 2021.
        aloud_ammount_on_turn (int, optional):Можно брать за раз. Defaults to 28.
    """
    list_of_players = [i for i in range(1,num_of_players+1)]
    i = 0
    while candy_ammount > 0 :
        if aloud_ammount_on_turn > candy_ammount:
            aloud_ammount_on_turn = candy_ammount
        candy_take = FUNC.input_number(f"Candy left : {candy_ammount} \tPlayer {list_of_players[i]} :")
        candy_ammount -= candy_take
        if candy_ammount == 0:
            break
        else :
            if i == num_of_players-1:
                i = 0
            else :
                i += 1

    print(f"Player {list_of_players[i]} took last candy ! he WON! ")




candy_ammount = 2021
aloud_ammount_on_turn = 28
num_of_players = 2

print(f"Игра - забери последнюю конфету !\nправила: есть {candy_ammount}\nза раз можно взять {aloud_ammount_on_turn}\nцель, забрать последнюю конфету !\n")
print(f'{game_players(num_of_players,candy_ammount,aloud_ammount_on_turn)}')

# print("есть выбор :\n1 - игра с компанией, от 2 до 6 человек\n2 - посмотреть как играют 2 бота\n4 - игра против слабого бота\n3 - игра против среднего бота\n")
# coise_case = FUNC.input_number_examination(text_in_input="Выш выбор : ", case_def= 3, min_num=1,max_num=4)
# match coise_case:
#     case 1:
#         num_of_players = FUNC.input_number_examination(text_in_input="Кол-во игроков от 2х до 6и : ", case_def= 3, min_num=2,max_num=6)
#         game_players(num_of_players,candy_ammount,aloud_ammount_on_turn)
  