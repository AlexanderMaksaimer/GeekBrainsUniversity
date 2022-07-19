# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import function as FUNC

print('Необходимо найти сумму элементов списка, находящихся на нечетной позиции')

list_of_numbers = FUNC.array_creation(10,1,25)

print(list_of_numbers)

def sum_number_odd_positions(list_of_numbers:list) -> int:
    """Count sum of elements thet are on not even positions
    Args:
        list_of_numbers (list): array of numbers 
    Returns:
        int: sum of elements at odd positions
    """
    # если индекс не чётный, то увеличиваем сумму на значение под этим индексом
    sum = 0
    index = 0
    for i in list_of_numbers:
        if index % 2 != 0:
            sum += i
        index += 1

    return sum
 
result = sum_number_odd_positions(list_of_numbers)
print(f"Сумма элементов на нечетных позициях в списке равняется:{result}")