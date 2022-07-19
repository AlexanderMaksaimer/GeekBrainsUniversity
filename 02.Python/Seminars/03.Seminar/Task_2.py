# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list_of_words = ["green","red","blue","yellow","yellow","yellow",]


# def task_gucntion(list_of_words):
#     index = 0
#     for i in list_of_words:
#         index +=1
#         index_second = index
#         for j in (list_of_words[index:]):
#             print(i,j)
#             if i == j:
#                 result = str(i) + " second time on index " + str(index_second)
#                 break
#             else:
#                 result = "No second"
#             index_second +=1
#         if result != "No second":
#             break
#     return result

# print(list_of_words)
# print(task_gucntion(list_of_words))

def findSecondIndex(list, word):
    n = 0
    for idx,item in enumerate(list):
        if (word == item):
            n += 1
            if (n == 2):
                return f'result = {idx}'
    return 'result - not found'

list_of_words = ['green', 'red', 'blue', 'yellow', 'green']
t = input('введите слово для поиска: ')
print(findSecondIndex(list_of_words, t))