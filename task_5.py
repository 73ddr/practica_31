def func_5():
    a = 0
    while True:
        numb = input("введите строку чисел, разделенных пробелами или * для выхода:").split()
        for i in numb:
            try:
                if i =="*":
                    print(f"сумма составляет {a}.Exit")
                    return
                else:
                    a += int(i)
            except ValueError:
                print("Введите число или * ")

        print(f"Cумма составляет {a}")

