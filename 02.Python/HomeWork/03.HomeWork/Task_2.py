# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import function as FUNC
print('Найдите произведение пар чисел списка')

def multiplication(list_of_numbers : list) -> list:
    """multiplication of pair in list (for example: 0,-1 / 1,-2)
    Args:
        list_of_numbers (list): array in wich multiplication will ocured
    Returns:
        list: list of multiplied pairs
    """
    # в середине перемножаем первый и последний эллемент, и добавляем результат в новый список
    multi_list = []
    for i in range (0,int(len(list_of_numbers)/2)):
        multi_list.append(list_of_numbers[i] * list_of_numbers[-(i+1)])
    # если кол-во эллементов нечётное, тогда средний эллемент возводим в квадрат
    if len(list_of_numbers) % 2 != 0:
        multi_list.append(list_of_numbers[len(list_of_numbers) % 2+1] ** 2)
    return multi_list

list_of_numbers = FUNC.array_creation(5,1,25)
result_list = multiplication(list_of_numbers)

print(f"Изначальный список : {list_of_numbers} => Результат произведений пар из списка : {result_list}")