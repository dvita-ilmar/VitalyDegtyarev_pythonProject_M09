"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.7
Домашнее задание по теме "Декораторы"
"""


# Функция-декоратор (добавляет функционал определения вида натурального числа)
def is_prime(func):

    # Функция-обёртка
    def wrapper(x, y, z):
        n = func(x, y, z) # Вызов основной функции

        # Обёртывание результата основной функции
        try:
            for i in range(2, n):
                if n % i == 0:
                    print('Составное')
                    return  n
        except TypeError:
            print('В аргументах функции присутствуют нецелые числа')
            return  n

        print('Простое')
        return n
    return wrapper


@is_prime # Обёртка
# Основная функция - складывающая любые числа
def sum_three(x, y, z):
    return x + y + z


# Запуск
if __name__ == '__main__':

    print(sum_three(2,3,3.5)) # В аргументах функции присутствует нецелые числа 8.5
    print(sum_three(2, 3, 6)) # Простое 11
    print(sum_three(7, 3, 6)) # Составное 16