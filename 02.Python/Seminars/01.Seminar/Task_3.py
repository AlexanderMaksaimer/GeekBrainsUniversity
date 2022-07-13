## 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

import math

number = int(input("Enter number : "))


if number < 0:
    number = -number

list_of_number = []

for num in range(-number,number+1):
    list_of_number.append(num)

print(list_of_number)

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

number2 = float(input("Enter number : "))

# result = math.floor(number2 % math.floor(number2)*10)
# print(f"{result}")

result = int(number2 * 10 % 10)

if result == 0:
    print(f"{number2} - > нет")
else :
    print(f"{number2} - > {result}")