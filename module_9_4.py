"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.4
Домашнее задание по теме "Создание функций на лету"
"""

from random import choice

# Запуск
if __name__ == '__main__':

# Lambda-функция:
    first = 'Мама мыла раму'
    second = 'Рама мыла маму'

    res = list(map(lambda x, y: x == y, first, second))
    print(list(res)) # [False, True, True, True, True, True, True, True, True, True, False, True, True, True]


# Замыкание:
    # Функция высшего порядка
    def get_advanced_writer(file_name):

        # Замыкающая функция
        def write_everything(*data_set):
            with open(file_name, 'w', encoding='utf-8') as file:
                for line in data_set:
                    file.write(str(line) + '\n')

        return write_everything

    # Вызов
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], ('А', 'это', 'вообще', 'не', 'подлежит'
            , 'изменению!'))


# Метод __call__:
    class MysticBall:

        def __init__(self, *words):
            self.words = list(words)

        # "Волшебный" метод, вызываемый как функция
        def __call__(self):
            return choice(self.words)

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball()) # Да|Нет|Наверное
    print(first_ball()) # Да|Нет|Наверное
    print(first_ball()) # Да|Нет|Наверное