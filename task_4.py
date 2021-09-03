def my_func_1(x, y):
    return 1 / x ** abs(y)

print(my_func_1(2, -2))


def my_func_2(x, y):
    for i in range(abs(y-1)):
        x *= x
        return 1 / x

print(my_func_2(8, -10))
