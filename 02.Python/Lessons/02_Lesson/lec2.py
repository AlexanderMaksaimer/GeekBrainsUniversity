# Данные, функции и модули

#Файлы
#Хранение данных
# Передача данных в клиент-серверных проектах
# Хранение конфигов
# Логирование действий

# Как работатать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных (если файла нет - он будет создан автоматически)
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

# with open('file.txt, 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file.txt','a')
data.writelines(colors) # разделителей не будет
data.write('n\LINE 2\n')
data.write('n\LINE 3\n')
data.close

exit()

path = 'file.txt' # создаем путь к файлу
data = open(path, 'r') # открываем в режиме чтения
for line in data: # при помощи цикла пробегаемся по файлу
    print(line) # считаем все строки
data.close() # после того как закончили чтение разорвем связь файловой переменной с файлом на диске

exit()

# функции и модули

import hello as h # вызов функции из другого файла и переименование его по своему усмотрению

print(h.f(1))

# функции

def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5)) # !!!!! (результат 5 символов воскл знак)
print(new_string('!'))    #TypeError missing 1 required (не указали значение count)

def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5)) # !!!!! (результат 5 символов воскл знак)
print(new_string('!'))    # !!!
print(new_string(4))      # 12 (перемножение, если ввести не символ, а число)

def concatenatio(*params): # для бесконечного количества аргументов функции (для этого в его описании ставить звездочку *)
    res: str = ""
    for item in params:
        res *= item
    return res

print(concatenatio('a', 'b', 'd', 'v')) #abdv
print(concatenatio('a', '1', 'd','2'))
    #print(concatenatio(1,2,3,4)) # TypeError: ....

# рекурсия (функция вызывающая сама себя)

def fib(n): # вычисление чисел Фибоначи
    if n in [1,2]: # Если n содержится в списке [1,2], то возвращаем 1
        return 1
    else: # иначе вычисление Фибоначи
        return fib(n-1) + fib(n-2)

list = []
for e in range (1,10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34 (первые 10 чисел)

#кортеж - неизменяемый список
a = (3, 4, 41, 4)
print(a)
print(a[-1])
a[0] = 12

t = ()
print(type(t)) #tuple
t = (1,)
print(type(t)) #tuple
t = (1)
print(type(t)) # int

t = (28, 9 , 1990)
print(type(t)) # tuple

colors = ['red', 'green', 'blue']
print(colors)   #('red','green','blue')
t = tuple(colors)
print(t)       #('red','green','blue')

a = (3,4,5)
print(a)
print(a[0])

for item in a:
    print(item)

t = tuple(['red','green','blue'])
print(t[0]) # red
print(t[2]) #blue
print(t[-2]) #green

for e in t:
    print(e)

t = tuple(['red','green','blue'])
red,green,blue = t
print('r:{} g:{} b:{}'.format(red,green,blue))
# r:red g:green b:blue

#Словари (Неупорядоченные коллекции произвольных объектов с доступом по ключу)
dictionary = {}
dictionary = \
    {
        'up':'вверх'
    }
print(dictionary)
print(dictionary['up'])
#типы ключей могут отличаться

for k in dictionary.keys(): #пробегаемся по ключам в словаре
    print(k)

for k in dictionary.values(): #пробегаемся по значениям в словаре
    print(k)

for v in dictionary: #пробегаемся по всем элементам словаря
    print(dictionary[v]) #чтобы вывести только значения

del dictionary['up'] # удаление элемента

dictionary['up'] = 'Vverh' # изменение конкретного элемента в словаре

for item in dictionary: # for (k,v) in dictionary items():
    print('{}:{}'.format(item,dictionary[item]))
    # up:
    # down:
    # right:

# Множества
