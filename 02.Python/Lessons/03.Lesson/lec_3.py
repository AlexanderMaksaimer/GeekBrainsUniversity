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

