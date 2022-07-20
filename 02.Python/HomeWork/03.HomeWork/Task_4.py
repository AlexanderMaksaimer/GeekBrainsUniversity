# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import function as FUNC
#Можно было сразу строкой:
# number = ''
# while n > 0:
# number = str(n % 2) + number
# n //= 2

def recode_number(number : int) -> list:
    """Recodes number in 2byte code
    Args:
        number (int): number that should be recoded
    Returns:
        list: 2 byte code of number
    """
    remainder = number 
    list_of_recode =[]
    # деление без остатка на 2. Остаток 1 или 0 пойдет в итоговый результат (в обратном порядке)
    # Процесс идет пока остаток больше 1
    while remainder >= 1:
        remainder = number // 2
        list_of_recode.append(number-remainder*2)
        number = remainder
    FUNC.array_turn(list_of_recode) # разворачиваем список / массив
    return FUNC.convert_array_to_integer(list_of_recode) # список в число переводим

number = FUNC.input_num_check_bigger_zero("Введите число (больше нуля) : ")
result = recode_number(number)
print('Преобразование десятичного числа в двоичное: ')
print(f"Изначальное число: {number} В десятичном виде => {result}")