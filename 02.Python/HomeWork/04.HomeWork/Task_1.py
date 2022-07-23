# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, 
# а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

import functions as FUNC
#from math import factorial
#from decimal import *

print('Вычислить число Пи c заданной точностью, \nиспользуя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских')
#пробовал почти все, но получилось именно по Нилаканту) в других видимо что то делал не так
number_d = FUNC.input_number("\nВведите желаемую точность (кол-во знаков после запятой) числа PI : ")

def pi_digit(number_of_iterations : int) -> float:
    """Calculation with the Nilakant formula
    Args:
        number_of_iterations (int): number of it iterations 
    Returns:
        float: returns Pi number
    """
    index = 2
    result = 3
    for i in range(1,number_of_iterations): 
        list_of_nums = list(map(int,[i for i in range(index,index+3)]))
        result_of_list = list_of_nums[0] * list_of_nums[1] * list_of_nums[2]
        index += 2
        if i%2!=0:
            result += 4/(result_of_list)
        else:
            result -= 4/(result_of_list)
    return result

print(f"Число Пи по формуле Нилаканта равняется: {round(pi_digit(number_of_iterations = 1000),number_d)}")

#остальные варианты не очень, но мб позже вернусь их доработать
# def pi_calc(number_of_iterations: int) -> float:
#     number_of_iterations = number_d
#     x = 1
#     series = []
#     for i in range(0,number_of_iterations):
#          value = (x**(2*i+1)*(-1)**i/(2*i+1))
#          series.append(value)
#     print (series)

# #result = pi_calc
#print(f'{pi_calc(number_d)}')


# def chudnovsky(number_d):
#     pi = Decimal(0)
#     k = 0
#     while k < number_d:
#         pi+=(Decimal(-1)**k)*(Decimal(factorial(6*k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3*k)))
#         k+=1
#         print('Шаг:{k} из {number_d}')
#     pi = pi * Decimal(10005).sqrt() / 4270934400
#     pi = pi**(-1)
#     return pi

# # Требуемая точность (число знаков после запятой)
# #N = 1000
# val = chudnovsky(number_d)
# print(val)
