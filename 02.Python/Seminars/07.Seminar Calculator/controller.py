import func as model
import input_data

def button_click():
    a = input_data.get_value()
    b = input_data.get_value()
    op = input("Введите оператцию: +, -, *, / \n")
    if op == "+":
        result = model.plus(a, b)
    elif op == "-":
        result = model.minus(a, b)
    elif op == "*":
        result = model.multiply(a, b)
    elif op == "/":
        result = model.devide(a, b)
    input_data.data(result)
    return result