"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.3
Домашнее задание по теме "Генераторные сборки"
"""


# Запуск
if __name__ == '__main__':
    # Исходные данные: (количество значений в списках должно быть одинаково)
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    # Генераторные сборки
    first_result = (abs(len(i)-len(j)) for i, j in zip(first, second) if len(i) != len(j))
    second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

    # Вывод результатов
    print(list(first_result)) # [1, 2]
    print(list(second_result)) # [False, False, True]