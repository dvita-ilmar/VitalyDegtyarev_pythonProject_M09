"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.5
Домашнее задание по теме "Итераторы"
"""


# Наше собственное исключение на соответствия выполнимости шага
class StepValueError(ValueError):
    pass


# Наш собственный итератор
class Iterator:

    # Инициализация итератора со значениями: старт, стоп, шаг (и счетчик)
    def __init__(self, start, stop, step=1):
        self.start = start
        # Проверка значения шага и выбрасывание исключения при 0-ыо шаге
        if step != 0:
            self.step = step
        else:
            raise StepValueError('Шаг не может быть равен 0')

        # Проверка значения шага и выбрасывание исключения при неверном векторе шага в диапазоне
        if stop - start > 0:
            if step > 0:
                self.step = step
            else:
                raise StepValueError('Шаг не может быть отрицательным')
        else:
            if step < 0:
                self.step = step
            else:
                raise StepValueError('Шаг не может быть положительным')

        self.stop = stop
        self.pointer = 0


    # Инициализация нашего итератора
    def __iter__(self):
        self.pointer = self.start - self.step # чтобы сама стартовая граница тоже вошла в итерацию
        return self

    # Итератор
    def __next__(self):
        self.pointer += self.step

        # Если счетчик пересечет границу стоп при положительном шаге
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration() # То стоп итерация

        # Если счетчик пересечет границу стоп при отрицательном шаге
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration()  # То стоп итерация

        return self.pointer


# Запуск
if __name__ == '__main__':

    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError as exc:
        print(exc) # Шаг не может быть равен 0

        iter2 = Iterator(-5, 1)
        iter3 = Iterator(6, 15, 2)
        iter4 = Iterator(5, 1, -1)

        for i in iter2:
            print(i, end=' ') # -5 -4 -3 -2 -1 0 1
        print()

        for i in iter3:
            print(i, end=' ') # 6 8 10 12 14
        print()

        for i in iter4:
           print(i, end=' ') # 5 4 3 2 1
        print()

    try:
        iter5 = Iterator(10, 1)
        for i in iter5:
            print(i, end=' ')
    except StepValueError as exc:
        print(exc) # Шаг не может быть положительным

    try:
        iter6 = Iterator(-3, 10, -3)
        for i in iter6:
            print(i, end=' ')
    except StepValueError as exc:
        print(exc) # Шаг не может быть отрицательным