# Лекция № 4. От простого к практике!
# Задача 0

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {x + y}')

def sum(a,b):
    return a+b

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x,y)}')

sum1 = lambda a, b: a+b

x1 = int(input('x = '))
y1 = int(input('y = '))
print(f'{x} + {y} = {sum1(x1,y1)}')

