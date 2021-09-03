def my_func(arg_1, arg_2, arg_3):
    a = [arg_1, arg_2, arg_3]
    a.remove(min(arg_1, arg_2, arg_3))
    return sum(a)

sum_num = my_func(44, 67, 3)
print(sum_num)
