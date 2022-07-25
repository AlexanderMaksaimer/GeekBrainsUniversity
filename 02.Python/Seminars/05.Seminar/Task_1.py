# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.



file = open('file.txt' , "r")
data = file.read()
list_of_rows = data.split()
file.close()

print(list_of_rows)

for i in range(1,len(list_of_rows)):
    if int(list_of_rows[i])-1 != int(list_of_rows[i-1]):
        print(f"should be {int(list_of_rows[i])-1}" )