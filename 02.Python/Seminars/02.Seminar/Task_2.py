# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from calendar import day_abbr
from functions import input_number_test_not_minus

number_n = input_number_test_not_minus("Enter n :")

dictionary_of_function = {}

for i in range(1,number_n+1):
    dictionary_of_function[i] = 3*i+1

print(dictionary_of_function)