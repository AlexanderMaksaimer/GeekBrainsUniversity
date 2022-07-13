# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from functions import input_number_test_biger_then_zero#проверка ввода на число, но убирает минусовые значения


#Я установил что первый эллемент списка 1, а потом формула - каждый эллемент - это предыдущий умножить на index +1 
number_n = input_number_test_biger_then_zero("Enter n : ")
list_of_numbers = [1]
for i in range(1,number_n):
    list_of_numbers.append(list_of_numbers[i-1]*(i+1))
print(list_of_numbers)