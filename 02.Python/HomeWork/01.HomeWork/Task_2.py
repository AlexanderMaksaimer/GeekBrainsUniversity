# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('x y z - Выражение № 1 - Выражение № 2')
for x in range (2):
    for y in range (2):
        for z in range (2):
            result1 = not x and not y and not z
            result2 = not(x or y or z)
            print(x,y,z, '-',result1, '-', result2)
if result1 == result2:
    print('Истинное равенство')
else:
    print('Ложное равенство')

