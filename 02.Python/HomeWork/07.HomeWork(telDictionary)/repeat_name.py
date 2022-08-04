# проверка ввода на повтор имени и фамилии в справочнике


import dictionaries
import json
        

def search(data):
    # Поиск по справочнику.
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Имя не найдено')