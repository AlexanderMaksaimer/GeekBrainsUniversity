# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time

print('Реализуйте выдачу случайного числа (или алгоритм перемешивания списка) без использования библеотеки рандом')
time_string = str(time.time_ns())

list_num = [1,3,5,7,9,11,25] 
print(list_num)

for i in range(0,len(list_num)):
    for j in time_string:
        if int(j) < len(list_num):
            list_num[i],list_num[int(j)] = list_num[int(j)],list_num[i]

print(list_num)