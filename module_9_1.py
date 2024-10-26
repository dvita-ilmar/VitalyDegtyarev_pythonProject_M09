"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.1
Домашнее задание по теме "Введение в функциональное программирование"
"""


# Функция высшего порядка (принимает список чисел и функции для работы со списком, возвращает словарь с названием функций и их результатами
def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list) # This is круто! Я в восторге от Python!
    return results


# Запуск
if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min)) # {'max': 20, 'min': 6}
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted)) # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}