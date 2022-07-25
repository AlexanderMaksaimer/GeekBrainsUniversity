# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    

list_input = [1, 5, 2, 3, 4, 6, 1, 7]


# for i in range(0,len(list_input)):
#     new_list = [list_input[i]]
#     print(i)
#     for j in range(i+1,len(list_input)):
#         if list_input[j] > max_in_list(new_list):
#             new_list.append(j)
#     new_list_dic[i] = new_list

# print(new_list_dic)

second_list_dic = {}

# for i,item in enumerate(list_input[:-1]):
#     new_list = [list_input[i]]
#     for j,item_2 in enumerate(list_input[i+1:]):
#         if item_2 > max_in_list(new_list):
#             new_list.append(item_2)
#     new_list_dic[i] = new_list

# for i,item in enumerate(list_input[:-2]):
#     new_list = [list_input[i]]
#     for j,item_2 in enumerate(list_input[i+2:]):
#         if item_2 > max_in_list(new_list):
#             new_list.append(item_2)
#     second_list_dic[i] = new_list

# print(new_list_dic)
# print(second_list_dic)

# index = len(new_list_dic)

# for i in second_list_dic.values():
#     if i not in new_list_dic.values():
#         new_list_dic[index] = i
#         index += 1
def max_in_list(list_of_numbers):
    max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max:
            max = i
    return max

new_list_dic = {}

index = 0

for n in range(1,len(list_input)):
    for i,item in enumerate(list_input[:-n]):
        new_list = [list_input[i]]
        for j,item_2 in enumerate(list_input[i+n:]):
            if item_2 > max_in_list(new_list):
                new_list.append(item_2)

            
        if new_list not in new_list_dic.values():
            new_list_dic[index] = new_list
            index += 1

for i in new_list_dic:
    print(f"{i} : \t{new_list_dic[i]}")

# a = [1, 5, 2, 3, 4, 6, 1, 7]


# def func(num):
#     my_list = []
#     my_list.append(a[num])
#     for i in range(num, len(a)):
#         if a[i] > my_list[-1]:
#             my_list.append(a[i])
#     print(my_list)


# for i in range(len(a)):
#     func(i)
