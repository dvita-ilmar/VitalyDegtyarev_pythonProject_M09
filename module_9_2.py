"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.2
Домашнее задание по теме "Списковые, словарные сборки"
"""


# Запуск
if __name__ == '__main__':

    # Исходные данные
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    # Списковые, словарные сборки
    first_result = [len(first_string) for first_string in first_strings if len(first_string) > 5]
    second_result = [(first_string, second_string) for first_string in first_strings for second_string in second_strings
                    if len(first_string) == len(second_string)]
    third_result = {string: len(string) for string in first_strings + second_strings if not len(string) % 2}

    # Вывод результатов
    print(first_result)
    print(second_result)
    print(third_result)