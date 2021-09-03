def func_div(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return "No value - error"


arg_1 = int(input("Введите любое положительное число:"))
arg_2 = int(input("Введите любое положительное число:"))
print(func_div(arg_1, arg_2))

