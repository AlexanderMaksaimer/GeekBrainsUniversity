from tkinter import *

from read_from_database import take_from_base as TAKE

def card_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')
    for item in data.values():
        if type(item) == dict:
            data_new = dict(item.items())

    for i,j in dict_of_rows.items():
        for y in range(2):
            if y == 0:
                Message(width=300, text=j) \
                    .grid(row=i, column=y, sticky=W)
            else:
                Message(width=300, text=data_new[j]) \
                    .grid(row=i, column=y)                
    window.mainloop()
    
def colums_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')
    new_list =[]
    new_list_index =[]
    for i,item in data.items():
        if type(item) == dict:
            data_new = dict(item.items())
        new_list.append(data_new)
        new_list_index.append(i)

    Message(width=300, text="ID") \
        .grid(row=0, column=0, sticky=W)
    for i in range(len(new_list_index)):
        Message(width=300, text=new_list_index[i]) \
            .grid(row=0, column=i+1 )
    for i,j in dict_of_rows.items():
        for y in range(len(data)+1):
            if y == 0:
                Message(width=300, text=j) \
                    .grid(row=i+1, column=y, sticky=W)
            else:
                Message(width=300, text=new_list[y-1][j]) \
                    .grid(row=i+1, column=y)          
    window.mainloop()