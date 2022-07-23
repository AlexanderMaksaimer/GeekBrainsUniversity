# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.

print('В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.')

file = open('Text.txt' , "w",encoding='utf-8')
file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
file.close()

path = 'Text.txt'

def remove_words_with_number(path: str) -> str:
    """Remove (delete) words with number from the text 
    Args:
        path (str): file path 
    Returns:
        str: Original text and processed text without words with number
    """
    file = open('Text.txt' , "r",encoding='utf-8')
    data = file.read()
    original_text = data.split()
    file.close()

    processed_text = []
    for i in original_text:
        delete_bool = False
        for n in i:
            if n.isdigit():
                delete_bool = True
                break
        if delete_bool == False:
            processed_text.append(i)

    return  f"Изначальный текст: {original_text} -> \nОтредактированный текст (без слов с цифрами):" + " ".join(processed_text) 
    
print(remove_words_with_number(path))