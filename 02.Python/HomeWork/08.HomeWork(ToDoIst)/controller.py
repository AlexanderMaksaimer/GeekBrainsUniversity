from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
import sqlite3
import json
import interface as UI

application_window = Tk()
application_window.title('MyDoList')
application_window.geometry('500x400')

i = None
interim_list = []
dictionary = {}

with open('ToDoIst_data.json', 'r', encoding='utf-8') as read_file:
    dictionary = json.load(read_file)

task_box = Listbox(selectmode=MULTIPLE, font=('Neuropol Medium', 11))
task_box.pack(fill = BOTH, expand = True)

# Спрашиваем имя пользователя
def hello_user ():
    user_name = input('\nДоброго времени суток. Напишите ваше имя: ')
    print(f'\nЗдравствуйте, {user_name}!Вы находитесь в приложении оформления списка дел',\
    'Чтобы добавить новое дело нажмите на кнопку "Добавить", для удаления - кнопку "Удалить"',\
    'Чтобы удалить все дела в списке - нажмите кнопку "Удалить все"',\
    'После завершения работы с приложением - нажмите "Выход"!')
    return user_name
    

def start():
    global conn
    global cur
    conn = sqlite3.connect("ToDoIst_data.json")
    cur = conn.cursor()

def begining(dictionary):
    if dictionary == {}:
        task_box.insert(END, 'На повестке дня дел не обнаружено')
    else:
        for i in dictionary:
            task_box.insert(END, str(i) + ')' + dictionary[i])
    for i in dictionary:
        interim_list.append(i)

begining(dictionary)
i = len(interim_list)+1

#print(dictionary)

view_all = 'ToDoIst_data.json'

def view_all_tasks(): #вывод всех задач

    with open(view_all, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])

def add_task(data_base: list): #создаем новую задачу
    print('Добавление новой задачи: ')
    cur.execute(data_base[0],data_base[1],data_base[2]) #описание, дата, статус выполнения
    conn.commit()
    return print("Новая задача добавлена")

def search_task(): #поиск через выпадающий список
    search = ComboBox(application_window)
    search['values'] = (dictionary)
    search.current(1)
    #search.grid(column = 0, row = 0)

def task_save_information(): #сохранение информации
    with open("ToDoIst_data.json", "w", encoding='utf-8') as write_file:
        json.dump(dictionary, write_file, indent=4, ensure_ascii=False)
    messagebox.showinfo("Успех!", "Информация сохранена")

def delete_one_task(): #удаление одной задачи
    select = list(task_box.curselection())
    select.reverse()
    for i in select:
        task_box.delete(i)
    messagebox.showinfo('Молодец', 'Отлично! Одним делом меньше!')

def delete_all_tasks(): #удаление всех задач
    global i
    task_box.delete(0, i)
    dictionary.clear()
    i = 1
    with open("ToDoIst_data.json", "w") as write_file:
        json.dump(dictionary, write_file, indent=4)
    messagebox.showinfo("Гуд жоб", "Все дела исполнены. Дел больше нет")

def ExitApp(): #выход из приложения
    exitmessage = messagebox.askquestion('Выход из приложения. Действительно хотите выйти?', icon = "error")
    if exitmessage == 'Да':
        application_window.destroy()
    else:
        messagebox.showinfo('С возвращением!=)')

task_label = UI.lable('Какова задача?:', "white", "black")
task_label.grid(row=1, column=0)

task_entry = UI.entry(application_window, 20)
task_entry.grid(row=1, column=1)

button_view_all_tasks = UI.button('Показать все дела(задачи)', view_all_tasks, "white", "green", 9)
button_view_all_tasks.grid(row=3, column=0)

button_view_all_tasks = UI.button('Поиск через выпадающий список', search_task, "grey", "green", 9)
button_view_all_tasks.grid(row=0, column=0)

button_add_task = UI.button('Добавить', add_task, "grey", "green", 8)
button_add_task.grid(row=1, column=2)

button_view_all_tasks = UI.button('Удалить всё', delete_all_tasks, "black", "red", 9)
button_view_all_tasks.grid(row=3, column=0)

button_save = UI.button('Сохранить', task_save_information, "grey", "orange", 8)
button_save.grid(row=2, column=2)

button_exit = UI.button('Выход из приложения', ExitApp, "grey", "red", 8)
button_exit.grid(row=2, column=1)

button_todo = UI.button('Удалить задачу', delete_one_task, "grey", "green", 8)
button_todo.grid(row=3, column=2)

application_window.mainloop()