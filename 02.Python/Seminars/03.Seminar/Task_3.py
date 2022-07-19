# 3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

from functions import input_number_test
import random

list_of_numbers = []
N = input_number_test("Enter N : ")
if N < 0:
    N *= -1

for i in range(-N,N+1):
    list_of_numbers.append(random.randint(1,10))

# file = open('file.txt' , "a")
# file.write("2\n3")
# file.close()

file = open('file.txt' , "r")
data = file.read()
list_of_rows = data.split()
file.close()

def multiply_Elemnts_in_array(list_of_numbers,list_of_rows):
    result = 1
    for i in range(0,len(list_of_rows)):
        result *= list_of_numbers[int(list_of_rows[i])]
    return result


print(list_of_numbers)
print(list_of_rows)
print(multiply_Elemnts_in_array(list_of_numbers,list_of_rows))