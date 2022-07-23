# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

import functions as FUNC

print('Задайте натуральное число N. Программа покажет список простых множителей числа N.')
input_number = FUNC.input_number('Введите натуральное число N: ') 
def simple_multipliers(number : int ) ->list:
    list_natural_numbers =[]
    number = input_number
    for j in range(2,input_number+1):
        for i in range(2,input_number+1):
            if number % i == 0:
                list_natural_numbers.append(i)
                number = number / i
                break
    return list_natural_numbers

list_simple_multipliers = simple_multipliers(input_number)
print(f"Для введенного числа: {input_number} Список простых множетелей -> {list_simple_multipliers} -> {set(list_simple_multipliers)}")