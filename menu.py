def menu(number, show_id):
    if number == 1:
        print("""=== МЕНЮ ===
        1. Войти
        2. Зарегистрироваться
        3. Прочитать сообщения
        4. Написать сообщение
        5. Действия администратора
        6. Настройки
        0. Выйти""")

    elif number == 2:
        print(f"""\n=== НАСТРОЙКИ ===
        1. Показ ID у сообщений - True/False - сейчас {show_id}
        0. Выход в меню
        Чтобы поменять параметр введите его номер и новое значение (1 True)\n""")
