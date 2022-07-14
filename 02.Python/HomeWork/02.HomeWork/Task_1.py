# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

from functions import input_number_test_float
print('Используем программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
number = str(input_number_test_float("Введите число : "))

result = 0
for i in number:
    if i.isdigit():
        result = result+int(i)

print(f"Сумма цифр введенного числа ({number}) равняется: {result}")