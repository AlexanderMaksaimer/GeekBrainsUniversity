# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача'
string_for_delete = "абв"

text_list = text.split()

final_list =[]
for i in text_list:
    if string_for_delete not in i:
        final_list.append(i)
print('Действие программы, удаляющей из текста все слова, содержащие "абв"\n')
result = " ".join(final_list)
print(f'Изначальный текст: {text}')
print(f"'Текст после удаления слов, содержащих '{string_for_delete}' -> '{result}'")