# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

from functions import input_number_test_float#как и советовали - тяну из файла проверку на число

number = str(input_number_test_float("Enter number : "))

result = 0

# схема - при вводе - проверяет на число, но сам number - строчка. По этому я прохожу по каждому эллементу строки, если число , тогда прибавляю к результату
for i in number:
    if i.isdigit():
        result = result+int(i)

print(f"sum of numbers in {number} = {result}")