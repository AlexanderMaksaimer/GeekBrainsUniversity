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