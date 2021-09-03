def pers_data(**kwargs):
    return kwargs

print(pers_data(name = input("Введите свое имя: "),
                 surname = input("Введите свою фамилию: "),
                 b_date = input("Введите дату своего рождения: "),
                town = input("Введите место(город) рождения: "),
                 email= input("Введите адрес электронной почты: "),
                 tel = input("Введите контактный телефон: "))
