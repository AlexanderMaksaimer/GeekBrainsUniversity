# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. (не использовать sort и sorted)

import functions as FUNC

list_of_numbers = FUNC.array_creation_random_int(10,0,10)

file = open('List_of_num.txt' , "w",encoding='utf-8')
for i in list_of_numbers:
    file.write(f"{i}\n")
file.close()

file = open('List_of_num.txt' , "r",encoding='utf-8')
data = file.read()

list_of_rows =data.split()
for i in range(0,len(list_of_rows)):
    list_of_rows[i] = int(list_of_rows[i])

def sort_list_from_min_to_max(list_of_nums : list):

    for i in range(0,len(list_of_nums)):
        for j in range(i+1,len(list_of_nums)):
            if list_of_nums[j] < list_of_nums[i]:
                list_of_nums[j],list_of_nums[i] = list_of_nums[i],list_of_nums[j]

print(list_of_numbers)
sort_list_from_min_to_max(list_of_rows)
print(list_of_rows)

file = open('List_of_num.txt' , "w",encoding='utf-8')
for i in list_of_rows:
    file.write(f"{i}\n")
file.close()