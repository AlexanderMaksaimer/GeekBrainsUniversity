print ('hello world')

#типы данных и переменная
# int, float, boolean, str, list, none
value = None
a = 123
b = 1.23
print (a)
print (b)
value = 12345
print (value)

print(type(a)) # type - для того чтобы показать тип данных  в переменной (int, float, str и тд.)
print(type(b))
print(type(value))

s = 'Hello World' # тип данных - строка
st = 'Hello \nWorld' # \n перенос на новую строку
print(s) # вывод строки

print(a, '-' , b, '-' , s) # вывод нескольких элементов за раз
print('{} - {} - {}'.format(a , b, s)) # вывод через .format
print(f'{a} - {b} - {s}') # вывод через интерполяцию

# логическая переменная (True / False)
f = True
print(f)

# массивы (подобие)
list = [1, 2, 3]
list2 = ['1', '2', '3', 'Hello World', 1 , 2.54, True] # Возможно иметь массив с разными типами переменных, но лучше так не делать
print(list)

# ввод и вывод данных
# input() print()

print = 'Введите a';
a = int(input())
print = 'Введите b';
b = int(input ())
print (a, b)
print ('{} {}'.format(a, b))
print (f'{a} {b}')

#Арифметические операции
#+, -, *, /, %, **, //
#Приоритетность : **, *, /, //, %, +, -,
# (), Сокращенные операции
a = 123
b = 456
c = a // b # Деление целых чисел
# / деление вещественных чисел
# % остаток от деления
# ** возведение в степень
c = round(a * b, 3) # round - округление по математическим правилам, 3 - количество символов после запятой
print(c)

a = 5
a += 3 # то же самое что и a = a + 3 (сокращение)
print(a)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# >, >=, <, <=, ==, !=
# not, and,  or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 3 # True / False
a = 'qwe'
b = 'qwe'
f = 1 < 4 or 5 > 10 # дизюнкция двух неравенств True когда хотя бы одно из неравенств True
f = [1,3,2,4]
print(f)
print (2 in f) # Найдет элемент в массиве и выдаст True / False 
print (not 2 in f) # Наоборот
print (a == b)

is_odd = f[0] % 2 == 0 # Остаток от деления на 2 равен нулю
is_odd = not f[0] % 2 # То же самое что и сверху
print(is_odd) # Остаток от деления True либо False

# Управляющие конструкции (if, if else)

# if else
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# elif

username = input('Введите имя:')
if username == 'Маша':
    print('Ура! Это же Маша!')
elif username == 'Марина':
    print('Добрый день, Марина')
elif username == 'Александр':
    print('Александр - топчик')
else:
    print('Привет, ' , username )

# Управляющие конструкции
# while

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original // 10
print(inverted)

#while else

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original // 10
else:
    print('Пожалуй,')
    print('Хватит')
print(inverted)

# for

for i in 1,2,3,4,5:
    print(i**2)


list = [1,2,3,4,5,10,7]
for i in list:
    print(i)

r = range (10) # диапазон от 0 до 9
for i in r:
    print(i)

for i in range (5): # диапазон до 5
    print(i)

for i in range(1, 10): # диапазон от 1 до 10
    print(i)

for i in 'qwe - rty': # пробег по строкам
    print(i)

# Немного о строках

text = 'сьешь еще этих мягких французских булок'

help(text.istitle) # подсказка в терминале по неизвестной команде

print(text[0]) # обращение к первому элементу строки
print(text(1)) # обращение ко второму элементу строки
print(text[len(text)]) # IndexError
print(text[len(text)-1]) # к (последний символ строки)
print(text[5]) # б (5 символ с конца строки)
print(text[:]) # print(text)
print(text[2:5]) #съ (от 2 до 5 символа)
print(text[6:-18]) # еще этих мягких (с 6 до -18 символа)
print(text[0:len(text):6]) #сеикакл

print(len(text)) # (определение количества символов)
print('еще' in text) # True (определение подстроки в строке используем оператор in)
print(text.isdigit()) # False (проверка являются ли все элементы строки числами)
print(text.islower()) # True (проверка являются ли все элементы символами нижнего регистра)
print(text.replace('еще', 'ЕЩЕ')) # (замена)

for c in text:
    print(c)

# Списки (введние)

numbers = [1,2,3,4,5]
print(numbers) # [1,2,3,4,5]

ran = range(1,6) # Диапазон
numbers = list(ran)
print(numbers) # [1,2,3,4,5]

numbers[0] = 10 # обращение к индексам [0]
print(f'{len(numbers)}len') # покажет длину списка / листа / масива
print(numbers) # [10,2,3,4,5]

for i in numbers:
    i *= 2
    print(i) # [20,4,6,8,10]
print(numbers) # [10,2,3,4,5]

colors = ['red', 'greeen', 'blue']

for e in colors:
    print(e) # red green blue

for e in colors:
    print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить элемент в конец
print (colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент

del colors [0]

# Функции

def f (x):
    if x == 1: 
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))