# Полезные фичи для Python

### Импорт функций из других баз:
В Python простая функция иморта "методов" из других файлов. Единственная особенность - файл с функциями должен быть в той-же папке что и основная программа.

Импорт только функции
```python
from functions import input_number_test

a = input_number_test("Enter text : ")
print(a)
```
где **`functions`** - название файла , а **`input_number_test`** - это название функции  

Импорт целого файла, как библиотеку ( не рекомендуется , что бы не грузить абсолютно все функции )

```python
import functions as fu

a = fu.input_number_test("Enter number : ")
print(a)
```
где **`functions`** - название файла , а **`fu`** - это будущее название библиотеки, используется как **`math`**

# Работа с файлами:

Хранение данных  
Передача данных в клиент-серверных проектах  
Хранение конфигов  
Логирование действий  

Метод испольщуется с аргументами:  
**`a`** - добавление в файл информацию(`append`)  
**`r`** - чтение информации из файла(`read`)  
**`w`** - перезапись файла(`write`)  

### Сам метод вызывается через :  

`with open() as data` - открыть как  
`data = open()` - присвоение перменной  
можно использовать адрес как переменную  
```python
with open('file.txt' , w) as data
data = open('file.txt' , w)
path = 'file.txt'
data = open(path , w)
```
### Функции которые используется  :  
`data.write()` - запись  
`data.writelines()` - запись в отдельную строчку  
`for line in data` - чтение  

```python
data.write("Hello world")
data.writeline("Hello world")
for line in date
    print(line)
```
```python
with open('test.txt', 'w') as test:
    for i in range ( 1 , 6):
        test.write(f"{i} - Hello World\n")
test.close()

test = open('test.txt','r')
list_of_lines =[]
for line in test:
    list_of_lines.append(line)


for i in range(0,len(list_of_lines)):
    print(list_of_lines[i])
test.close()

print(list_of_lines)
```
# Функции:
Запись функции:  

```python
def f(number):
    if number<0:
        return "minus"
    else
        return "plus"
```  
Варианты:  
где, symb = "" , задаётся параметр - при котором если его не ввести в функцию, используется значение по умолчанию. 
```python
def f(number,symb = ""):
    return number + symb + number
```  
где, *numbers - возможность ввести множество переменных
```python
def f(*numbers):
    for i in numbers:
        result += i
    return result
```  
Рекурсия :
```python
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
```  
# Кортежи:
Кортеж создаётся через (), пример: t = ()
```python
t = (1 , 234 , 5)
```  
Вызов эллемента картежа как и через списко, пример t[0]  
**`ВАЖНО!`** в кортеже невозможно перезписывать данные
```python
print(t[0])
```  
Создание кортежа из списка , пример t=tuple([red,green,blue])
```python
colors = ['red','green','blue']
t = tuple(colors)
```  
вывод переменной из картежа, пример red,grenn,blue = t
```python
colors = ['red','green','blue']
t = tuple(colors)
red,grenn,blue = t
```  
# Словари:
Словарь создаётся через {}, пример: t = {}  
В словаре обязательная пара Ключ `:` Значение
```python
t = {1 : "Wn", 5 : "Fr"}
```
Работа с эллементами, примерр t(1) = "Tr"
Перезапишет эллемент с ключём 1
```python
t(1) = "Tr"
```
Проход по всем эллементам словаря
```python
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
 ```
 удаление эллемента словаря
 ```python
del dictionary['left'] # удаление элемента
 ```
 Прочее:  
-   key - ключ
-   value - значение
-   items - эллементы
# Множества:
Это набор **`НЕПОВТОРЯЮЩИХСЯ`** значений
создаётся через {}, пример t = {1,2,3,4,5}


``` python
colors = {'red', 'green', 'blue'}
colors.add('red') #добавить
colors.remove('red') #убрать
colors.discard('red') 
colors.clear() #очистить

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # скопировать
u = a.union(b) # объеденить
i = a.intersection(b) # пересечение
dl = a.difference(b) # разность
```

``` python
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
```