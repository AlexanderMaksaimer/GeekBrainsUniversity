# 2- Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

from functions import fibonachi_result

print('Задайте последовательность чисел. Выведите список неповторяющихся элементов исходной последовательности.')

fibonachi_sample = fibonachi_result(12)

print(f"Заданная последовательность чисел : {fibonachi_sample}") # взял фибоначи, тк уже готовая последовательность после предидущего дз=)

def nonrepeatable_numbers_in_array(list_of_numbers : list) ->list:
    """Create new array with non-repeatable elements
    Args:
        list_of_numbers (list): Original array
    Returns:
        list: New array with non-repeatable elements
    """
    new_list_numbers =[list_of_numbers[0]]  
    for i in list_of_numbers:
        index = 1
        for j in new_list_numbers:
            if i == j:
                index +=1
        if index == 1:
            new_list_numbers.append(i)
    return new_list_numbers

print(f"Список неповторяющихся элементов : {nonrepeatable_numbers_in_array(fibonachi_sample)}")