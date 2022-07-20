# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.


str_of_num = input("Enter numbers usign space : ")

list_of_nums = str_of_num.split()

for i in range(0,len(list_of_nums)):
    list_of_nums[i] = int(list_of_nums[i])

max_num = list_of_nums[0]
min_num = list_of_nums[0]

for i in list_of_nums:
    if i<min_num:
        min_num = i
    if i>max_num:
        max_num = i

print(f"{list_of_nums} min : {min_num} and max : {max_num}")