# 3 - Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5.561, 10.01] => 0.56 или 56

import function as FUNC

def check_min_max_fractional_numbers(list_of_numbers : list) -> int:
    """Search min and max value of fraction part in float numbers in array
    Args:
        list_of_numbers (list): array of float numbers
    Returns:
        int: min and max fractional numbers
    """
    # проходим по списку дробных числе и проверяем больше максимума - записываем в максимум, меньше минимума - записываем в минимум
    max = list_of_numbers[0] - int(list_of_numbers[0])
    min = list_of_numbers[0] - int(list_of_numbers[0]) 
    for i in list_of_numbers:
        number = i - int(i)
        if number > max:
            max = number
        if number < min:
            min = number
    return min,max


list_of_num = FUNC.array_creation_float(10)
print('Список дробных элементов:',list_of_num)
min,max = check_min_max_fractional_numbers(list_of_num)
result = max - min
print('Необходимо найти разницу между максимальным и минимальным значением дробной части элементов')
print(f"Max({max:.4f}) - Min({min:.4f}) = {result:.4f}")