# 2- Найти сумму чисел списка стоящих на нечетной позиции

def sum_elements(list_of_num : list):
    sum_of_num = 0
    for i in list(filter(lambda a : list_of_num.index(a)%2 != 0  , list_of_num)):
        sum_of_num += i
    return sum_of_num

list_of_num = [1,2,3,4,5,6,7,8,9]
print(f"Список :{list_of_num} \n Сумма элементов на нечетных позициях {sum_elements(list_of_num)} ")