# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, 
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]

print('Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.\n')

programming_languages = ["Python","C++","C#","GoLang","Ruby","JAVA","HTML","JAVASCRIPT"]
language_upper = list(map(str.upper, programming_languages))
list_numbers = [i for i in range(1,len(language_upper)+1)]

result_list = list(zip(list_numbers,language_upper))
print('Функция № 1: список кортежей, состоящих из номера и ЯП, написанного большими буквами')
print(result_list)

new_result_list = []
for i,item in enumerate(result_list):
    sum_points = 0
    for j in item[1]:
        sum_points += ord(j)
    print(f"{result_list[i][1]} => {sum_points} % {result_list[i][0]} => {sum_points%result_list[i][0] == 0}")
    if sum_points%result_list[i][0] == 0:
        new_result_list.append((sum_points,item[1]))
print('Функция № 2: Отфильтровать следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков')
print(new_result_list)
