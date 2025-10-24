from math import sqrt


def safe_apply(func, data):
    results = []  # список для сохранения успешных результатов
    errors = []  # список для сохранения пар (элемент, исключение)

    for item in data:
        try:
            result = func(item)
            results.append(result)
        except Exception as e:
            errors.append((item, str(e)))  # Сохраняем сам элемент и текст ошибки

    return results, errors


# Демонстрация работы функции
data_list = ['4', '16', 'text', '-25', '9.0']
func_to_apply = lambda x: float(x) ** 0.5  # Функция, извлекающая квадратный корень

results, errors = safe_apply(func_to_apply, data_list)

print("Results:", results)
print("Errors:", errors)