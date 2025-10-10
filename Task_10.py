while True:
    user_input = input("Введите число: ")

    if user_input.lower() == "стоп":
        break

    try:
        number = float(user_input)
        print(f"Введённое число: {number}")

    except ValueError:
        print("Ошибка: введите число или 'стоп'.")