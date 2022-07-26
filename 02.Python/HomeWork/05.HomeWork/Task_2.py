# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import functions as FUNC
import random


all_candies = 2021
max_candies_for_turn = 28

def bot_for_game(candy_total=2021,candies_one_turn = 28):
    """Игра против бота, который рандомно берет конфеты
    Args:
        all_candies (int, optional): Всего конфет. По заданию 2021.
        max_candies_for_turn (int, optional): Количество конфет, которые можно взять за 1 ход. В нашем случае 28.
    """
    begin = input("Нажмите любую кнопку для начала игры")
    definition = random.randint(0,2)
    if definition == 0:
        players = ["Игрок № 1","Игрок № 2"]
        print("Игрок № 1 делает первый ход \n")
    else:
        players = ["Игрок № 2","Игрок № 1"]
        print("Игрок № 2 делает первый ход \n")
    i = 0
    while candy_total > 0 :
        if candies_one_turn > candy_total:
            candies_one_turn = candy_total
        if players[i] == "Игрок № 1":
            move_candy = FUNC.input_number(f"Остаток : {candy_total} \t{players[i]} :")
        else:
            move_candy = random.randint(1,candies_one_turn)
            print(f"Остаток : {candy_total} \t{players[i]} : {move_candy}")
        candy_total -= move_candy
        if candy_total == 0:
            break
        else :
            if i == 1:
                i = 0
            else :
                i = 0

    print(f"Игрок {players[i]} взял последнюю конфету! ")

print(f"Игра - забери последнюю конфету !\n: есть {all_candies} конфет\nза один ход можно взять {max_candies_for_turn} конфет\nзадача - забрать последнюю конфетку !\n")
print(f'{bot_for_game(all_candies,max_candies_for_turn)}')
  