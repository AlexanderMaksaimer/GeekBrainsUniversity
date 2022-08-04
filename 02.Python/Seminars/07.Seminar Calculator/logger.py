from datetime import datetime as dt
from time import time

def check(data):
    time = dt.now().strftime("%h:%m")
    with open("new_file.csv", "a") as file:
        file.write("\n{}; value; {}".format(time, data))