#Можем положить функцию в какую-либо переменную
from typing import Iterable


def f(x):
    x**2

g = f
print(f(1))
print(g(1))

#если можем фукнцию передать в качестве аргумента в другую функцию

def f(x):
    return x**2

print(f(2))

#чтобы сократить такой код, в случае если мы вызываем функцию всего один(1) раз за все время работы приложения, то можно сократить код

def f(x):
    return x**2

g = f
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

def calc(x):
    return x+10

print(calc(10))

def calc2(x):
    return x*10

print(calc2(10))

def math(op,x):
    print(op,(x))

math(calc2,10)
math(calc,10)

def sum (x,y):
    return x+y

f = sum
sum = lambda x, y: x+y #то же что написано выше

def mylt(x,y):
    return x*y

def calc(op,a,b):
    print(op(a,b))
    #return op(a,b)
# в качестве аргумента передаем функцию
calc(f, 4, 5)

# Лямбда - 

calc(lambda x,y:x+y, 4,5)

# List Comprehension
#Быстрое создание списков:

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

list = []

for i in range(1,101):
    #if(i%2 == 0):
        list.append(i)

print(list)

list = [i for i in range(1,21)]
print(list)

# сократили то что было с 74 по 76 строку 
list = [i for i in range (1,21) if i % 2 == 0]
print(list)

#список картежей
list = [(i,i) for i in range(1,21) if i % 2 == 0]
print(list)

def f(x):
    return x**3
#чтобы показать число и его кубы
list = [(i,f(i)) for i in range(1,21) if i % 2 ==0]
print(list)

#Задача: в файле хранятся числа, нужно выбрать четные и составить список пар (число;квадрат числа)
#пример: 1 2 3 5 8 15 23 38
#получить: [(2,4),(8,64),(38,1444)]
path = '/Users/'        #путь к файлу
f = open (path, 'r')    # связываем файловую переменную с файлом на диске
data = f.read() + ' '   # считываем все то есть в файле + добавляем пробел
f.close()               # закрываем файл

numbers = []            # создаем пустой список, который в дальнейшем будем наполнять

while data != '':       # пробегаемся по строке, которую считали выше и делаем проверки: пока моя строка не пустая (пробел)
    space_pos = data.index(' ')  # находим первую позицию пробела
    numbers.append(int(data[:space_pos]))  # берем все что находится от первой позиции до позиции пробела, превратить это в число и добавить список номеров и добавить список чисел
    data = data[space_pos+1:] # обновить строку с учетом того что ТО, что мы уже добавили в нашу строку обработали и больше это не нужно использовать

out = []                #создаем новый список
for e in numbers:       #пробегаемся по исходному списку Намберс
    if not e % 2:       # проверка условия что число является четным
        out.append((e,e **2))  #добавить новый список - картежи, где первый элемент это число, а второй элемент это квадрат этого числа
print(out)


def select(f, col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int,data)
res = where(lambda x: not x % 2, res) # описываем Лямбду, которая будет проверять Х и возвращать результат для четных чисел (Х остаток от деления на 2), 
                                        #в качестве второго аргумента передаем результат работы на предидущем этапе
# ожидаем увидеть список только четных чисел

res = select(lambda x:(x,x**2),res)  #снова функция Селект, которая вернет картеж Х и Х в квадрате

print(res)


# Функция 'map()'
# которая применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами

#f(x) = x + 10
map(f,[1 , 2, 3, 4, 5])

#нельзя пройтись дважды! результат работы MAP - итератор, по которому можно пробежаться всего один (1) раз

li = [x for x in range(1,20)]

li = list(map(lambda x: x+10, li)) 

print(li)


data = list(map(int,input().split())) # превращаем лист из строк в лист чисел 
                         #чтобы превратить это в НАБОР данных нужно поставить list перед map. Для приведения к типу list 


print(data)


def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int,data)
res = where(lambda x: not x % 2, res) # описываем Лямбду, которая будет проверять Х и возвращать результат для четных чисел (Х остаток от деления на 2), 
                                        #в качестве второго аргумента передаем результат работы на предидущем этапе
# ожидаем увидеть список только четных чисел

res = list(map(lambda x:(x,x**2),res))  #через map

print(res)


# функция filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта 
# и возвращает итератор с теми объектами, для которых функцию вернула True

data = [x for x in range(10)]

res = (filter(lambda x: not x%2, data)) #фильтр четных чисел


print(res)

#ранее описанный код в оптимизированном виде выглядит как : через map и filter
data = '1 2 3 5 8 15 23 38'.split()

res = map(int,data)
res = filter(lambda x: not x % 2, res) # описываем Лямбду, которая будет проверять Х и возвращать результат для четных чисел (Х остаток от деления на 2), 
                                        #в качестве второго аргумента передаем результат работы на предидущем этапе
# ожидаем увидеть список только четных чисел

res = list(map(lambda x:(x,x**2),res))  #через map

print(res)

# Функция zip (). еще одна функция для обработки данных
#Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входгных данных
# Количество элементов в реультате равно минимальному количеству элементов входного набора
#Нельзя пройтись по нему дважды
#Пример:
zip ([1,2,3],['о','д','т'],['f','s','t'])
[(1,'o','f'),(2,'д','s'),(3,'т','t')]

#Будет сформирован 1 элемент из первых элементов первого набора, второй набор из вторых элементов второго набора, 
# и третий элементо и третьих элементов третьего набора

users = ['user1','user2','user3','user4']
ids = [4,5,9,14,7]
salary = [111,222,333]

data = list(zip(users,ids,salary))


#Функция enumerate - позволяет пронумеровать 
#Функция enumerate() применяется к итерируемому объекту 
# и возвращает новый итератор с кортежами из индекса и элементов входных данных.

#нельзя пройтись дважды

users = ['user1','user2','user3','user4']
ids = [4,5,9,14,7]
salary = [111,222,333]

data = list(enumerate(users,ids,salary))
print(data)


