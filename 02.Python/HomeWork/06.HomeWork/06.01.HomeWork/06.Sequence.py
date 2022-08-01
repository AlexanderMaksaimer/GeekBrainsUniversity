# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import functions as FUNC
print('Сформировать список из  N членов последовательности.')
def sequence(number_N):
    list_of_num = [1]
    for i in range(1,number_N):
        list_of_num.append(list_of_num[i-1]*-3)
    return list_of_num

number_N=FUNC.input_number('Введите число N = ')
print(f"Для числа N = {number_N} последовательность: {sequence(number_N)}")