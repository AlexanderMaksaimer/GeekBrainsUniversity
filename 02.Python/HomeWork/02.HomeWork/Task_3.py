# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

from functions import input_number_bigger_then_zero

print('Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.')
number_n = input_number_bigger_then_zero("Введите N : ")

dict_of_numbers = {}

# как на семинаре
for i in range(1,number_n+1):
    dict_of_numbers[i] = (1+1/i)**i
print(dict_of_numbers)

result = 0

for i in dict_of_numbers:
    result += float(dict_of_numbers[i])
print(f"Сумма элементов равняется: {result:.2f}") # ограничил двумя знаками после запятой