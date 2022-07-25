# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абвгдейка - это передача'
str_to_delete = "абв"

list_text = text.split()

result_list =[]
for i in list_text:
    if str_to_delete not in i:
        result_list.append(i)

resutl = " ".join(result_list)
print(f"'{text}' without '{str_to_delete}' -> '{resutl}'")