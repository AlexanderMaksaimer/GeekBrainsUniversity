# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/sH87m)

import function as FUNC

print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
#решение вышло не оптимальным (через 3 функции), буду рад если скажите что добавить для решения через одну. 
#Думал можно просто умножить второй элемент в первом списке, 
#однако почему то все равно выдавал только положительные (либо последовательность 0 0 1 1 -1 -1 и тд), 
# поэтому решил создать не через 1, а через 3 массива (+ - и общий)

def fibonachi_positive(fib_range : int) -> list: # положительный фибоначи
    """Create array with positive numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci numbers
    Returns:
        list: positive part of Negafibonachi
    """
    array_fibonachi = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            array_fibonachi.append(array_fibonachi[i-1]+array_fibonachi[i-2])
    return array_fibonachi

def fibonachi_negative(fib_range : int) -> list: # отрицательный фибоначи. 
    """Create array with negative numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci numbers
    Returns:
        list: negative part of Negafibonachi
    """
    array_fibonachi = [0,1]
    if fib_range > 1:
        for i in range(2,fib_range+1):
            array_fibonachi.append(array_fibonachi[i-2]-array_fibonachi[i-1])
    return array_fibonachi

def fibonachi_result(fib_range : int) -> list:
    """Create genaral array with positive and negative numbers of fibonachi
    Args:
        fib_range (int): range of fibonacci 
    Returns:
        list: general array
    """
    positive = fibonachi_positive(fib_range) 
    negative = fibonachi_negative(fib_range) 
    FUNC.array_turn(negative) # разворачиваем минусовой фибоначи при помощи функции разворота массива
    for i in range(1,fib_range+1): # к минусовому массиву добавляем положительный по каждому эллементу
        negative.append(positive[i])
    return negative
        
fib_range = FUNC.input_num_check_bigger_zero("Введите количество элементов Фибоначи (k): ")
result_array_negafibonachi = fibonachi_result(fib_range)
print(f"При k = {fib_range} последовательность Негафибоначи будет выглядеть: {result_array_negafibonachi}")
