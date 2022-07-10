# Напишите программу, которая найдет максимальное из 5 чисел и выведет на экран

list = [1,20,5,75,42]

def function(b):
    max = b[0]
    for i in b:
        if i > max:
            max = i
    return max

print('Максимальное число =', function)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
import random
number_ammount = int(input("Enter number's ammount : "))

i=0
list_numbers =[]

while i < number_ammount:
    number = int(input("Enter number : "))
    list_numbers.append(number)
    print(list_numbers[i])
    i+=1

max = list_numbers[0]

for num in list_numbers:
    if max<num:
        max = num

print("{} is max ".format(max))