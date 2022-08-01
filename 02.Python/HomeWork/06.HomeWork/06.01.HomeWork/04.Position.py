# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def look_up_second_pos(list_letters,str_search):
    count = 0
    for i,item in enumerate(list_letters):
        if item == str_search:
            count +=1
            if count ==2:
                break
    if count>0:
        return i
    else:
        return -1

    

text = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
need_find = "qwe"

print(f"список: {text}, ищем: '{need_find}', ответ: {look_up_second_pos(text,need_find)}")