# 4.Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

import functions as FUNC

number_one = FUNC.input_number_examination(text_in_input="Entert number A : ",case_def=1)
number_two = FUNC.input_number_examination(text_in_input="Entert number B : ",case_def=1)

NOK_bool = True
NOK_num = 2

# while NOK_bool and NOK_num<1000:
#     NOK_num += 1
#     if number_one % NOK_num == 0 and number_two % NOK_num == 0:
#         NOK_bool = False

while NOK_bool:
    NOK_num += 1
    if NOK_num % number_one  == 0 and NOK_num % number_two  == 0:
        NOK_bool = False

print(f"For {number_one} and {number_two} NOK is : {NOK_num}")


a,b = int(input('Enter A :')), int(input('Enter B :'))
num = (a,b)
res = []
for i in range(max(num), a*b+1):
    if i%a == 0 and i%b == 0:
        res.append(i)
# print(res)
print(min(res))