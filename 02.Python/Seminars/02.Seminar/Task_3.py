# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
str_one ='Говорит попугай попугаю:". Я тебя, попугай, попугаю". Отвечает ему попугай:". Попугай, попугай, попугай!".'
str_two ='попуг'
# str_one = str(input("Enter string 1 : "))
# str_two = str(input("Enter string 2 : "))

count = 0

#print(len(str_one)-len(str_two))
for i in range(0,len(str_one)-len(str_two)):
    #print(str_one[i:i+len(str_two)])
    if str_two.lower() == str_one[i:i+len(str_two)].lower():
        count +=1
print(f"IN {str_one} word {str_two} {count} times")