import datetime
import os


def logger(string: str):
    time = datetime.datetime.today()
    print(time)
    string_result = str(time) + ' | ' + string
    print(string_result)
    with open(path, 'a') as writer:
        writer.write(string_result + '\n')


path = os.path.join('Logs', 'logs.csv')