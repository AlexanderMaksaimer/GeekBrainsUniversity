# библиотека которая позволяет делать проверку числа на четность
# from isOdd import isOdd

# print(isOdd('1')) 
# print(isOdd('5')) 

# print(isOdd(0)) 
# print(isOdd(4)) 

#библиотека с прогресс Баром (имитация загрузки)
# from progress.bar import Bar
# import time #взяли время для визуального отображения
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1) #задержка в 1 секунду между итерациями загрузки
#     bar.next()
# bar.finish()

# #библиотека с Эмоджи(смайлики)
# import emoji
# print(emoji.emojize('Python is :thumbs_up:')) #Python is 👍


#библиотека с визуальным представлением графиков (matplotlib)
# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

#пример графика
# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,4,2,6]
# plt.plot(list)
# plt.show()

