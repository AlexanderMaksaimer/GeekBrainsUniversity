# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import functions as FUNC
import random

def input_positions_in_txt():
    """Ввод позиций в ручную, через проблем
    """
    str_of_num = input("Enter numbers usign space : ")
    list_of_nums = str_of_num.split()

    file = open('Position.txt' , "w",encoding='utf-8')
    for i in list_of_nums:
        file.write(f"{i}\n")
    file.close()

def input_random_positions_in_txt(ammount_of_pos: int,number_N: int):
    """Генератор случайных позиций
    Args:
        ammount_of_pos (int): кол-во позиций
        number_N (int): Подвязка к переменной N
    """
    file = open('Position.txt' , "w",encoding='utf-8')
    for i in range(0,ammount_of_pos):
        file.write(f"{random.randint(0,number_N*2)}\n")
    file.close()

number_N= FUNC.input_number_examination(text_in_input='Enter N :' , case_def=1)

if number_N<0:
    number_N *= -1

list_of_numbers = []

for i in range(-number_N,number_N+1):
    list_of_numbers.append(i)

choose_metod = FUNC.input_number_examination(text_in_input="1 - Enter throu board or 2 - Random : ",case_def=3,min_num=1,max_num=2)

match choose_metod:
    case 1 :
        input_positions_in_txt()
    case 2:
        ammount_of_pos = FUNC.input_number_examination(text_in_input="Enter ammount of positions fo random : ")
        input_random_positions_in_txt(ammount_of_pos = ammount_of_pos,number_N=number_N)

file = open('Position.txt' , "r",encoding='utf-8')
data = file.read()

list_of_rows =data.split()
list_of_num_to_mult = []
result = 1

for i in list_of_rows:
    if i.isdigit():
        i = int(i)
        if i<len(list_of_numbers) and i>= 0:
            result *= list_of_numbers[i]
            list_of_num_to_mult.append(f"{i} : {list_of_numbers[i]}")

print(f"{list_of_numbers} -> {list_of_num_to_mult} -> {result}")