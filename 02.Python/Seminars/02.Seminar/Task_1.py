# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


from functions import input_number_test_not_minus

number_N = input_number_test_not_minus("Enter N : ")

list_of_numbers = []
list_of_numbers.append(1)

for i in range(0,number_N-1):
    list_of_numbers.append(list_of_numbers[i]*-3)

print(list_of_numbers)