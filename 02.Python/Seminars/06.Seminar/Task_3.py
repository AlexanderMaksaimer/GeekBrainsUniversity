# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list_of_numbers = [1, 2, 3, 5, 1, 5, 3, 10] 

def list_with_no_(list_of_numbers : list) ->list:
    new_list = []
    for i in list_of_numbers:
        if list_of_numbers.count(i) == 1:
            new_list.append(i)
    return new_list

print(f"{list_of_numbers} -> {list_with_no_(list_of_numbers)}")