import json

data = {
    1: {
"todo": "Сказать про json",
"status": "new"
}
}

def read_file(filename: str) -> dict:
    """
    Выгружает в память словарь с данными из JSON файла.
    :param data.json имя файла.
    :return: словарик
    """
    data_base = {}
    try:
        with open("data_file.json", "r", encoding='utf-8') as read_file:
            data_from_file = json.load(read_file, object_hook=_decode)
        #open('data.json', 'r', encoding='utf-8') as file:
            #db = json.load(file)
            for row in data_from_file:
                data_base[int(row[0])] = {
                    'TASK': str(row[1]),
                    'STATUS': int(row[2])
                }
    except FileNotFoundError:
        print('Файл не обнаружен.')
    return data_base

data_base_tasks = read_file('data.json')

def add_task(task: dict, arg: str) -> str:
    new_task = arg 
    data_base_new = {
        'TASK': new_task,
        'STATUS': 0
    }
    task = data_base_new
    with open("data_file.json", "w", encoding='utf-8') as write_file: #Запись:
            json.dump(data, write_file,#запись в файл
                ensure_ascii=False,#можно не ASCII-символы - для русского языка
                indent = 4) #отступы 
    # open('data.json','w',encoding='utf-8') as file:
    #     file.write(json.dumps(task))
    return f"Ваша задача => {new_task} => добавлена."
    
#На выходе получается именно словарь! Такой же, как выше в data, но за одним исключением: id выходит строкой. Берем код из интернета:
def _decode(o):
    if isinstance(o, str):
        try:
            return int(o)
        except ValueError:
            return o
    elif isinstance(o, dict):
        return {k: _decode(v) for k, v in o.items()}
    elif isinstance(o, list):
        return [_decode(v) for v in o]
    else:
        return o

def del_task(task: dict, ID: str) -> str:
    try:
        delete = abs(int(ID))
    except ValueError:
        return f"Ошибка ввода, юный падован"
    if delete in task.keys():
        del task[delete]
        return f"Ваша задача => {delete} => удалена."
    else:
        return f'ID# => {delete} не найден'


def info_save(task: dict) -> str:
    with open('data.json', 'w', encoding='utf-8', newline='') as file:
        save_task = json.dumps(file)
        for k, v in task.items():
            new_info = [k, v['TASK'], v['STATUS']]
            save_task.writerow(new_info)
    return 'Информация сохранена, юный падован'


def task_print(task_list: dict, status: int) -> str:
    list_temp = []
    if status == 1:
        for key, value in task_list.items():
            list_temp.append(f'ID {key} => {value["TASK"]} => {"Выполнено" if value["performed"] else "Не выполнено"}')
        return '\n'.join(list_temp)
    elif status == 2:
        for value in task_list.values():
            for k, v in value.items():
                if k == 'performed' and v:
                    list_temp.append(value['TASK'])
        return '\n'.join(list_temp)
    elif status == 3:
        for value in task_list.values():
            for k, v in value.items():
                if k == 'performed' and not v:
                    list_temp.append(value['TASK'])
        return '\n'.join(list_temp)
