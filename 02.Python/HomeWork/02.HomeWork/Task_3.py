# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

from functions import input_number_test_biger_then_zero

number_n = input_number_test_biger_then_zero("Enter n : ")

dict_of_numbers = {}

# это мы на семинаре делали, не буду останавилваться 
for i in range(1,number_n+1):
    dict_of_numbers[i] = (1+1/i)**i
print(dict_of_numbers)

result = 0
# а тут высчитывается сумма эллементов , со второй попытки понял что в данном случае for проходится по ключам =) 
for i in dict_of_numbers:
    result += float(dict_of_numbers[i])
print(f"Sum of ellements is {result:.3f}")