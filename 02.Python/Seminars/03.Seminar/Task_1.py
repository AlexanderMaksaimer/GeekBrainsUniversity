# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from queue import Empty
import random

from functions import input_number_test

list_of_number = []
for i in range(1,20):
    list_of_number.append(random.randint(1,10))

look_up_number = input_number_test("Enter number to look up : ")

def look_up_number_in_list(list_of_number,look_up_number):
    result = Empty
    for num in list_of_number:
        if num == look_up_number:
            result += str(look_up_number) + " is in list"
            break
        else:
            result += str(look_up_number) + " not in list"
    return result

print(list_of_number)
print(look_up_number_in_list(list_of_number,look_up_number))