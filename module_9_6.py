"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №9.6
Домашнее задание по теме "Генераторы"
"""


# Генератор подпоследовательности символов принятой строки
def all_variants(text):
    for i in range(len(text)+1):
        for j in range(i+1, len(text)+1):
            yield text[i:j]


# Запуск
if __name__ == '__main__':

    a = all_variants("abc")
    for i in a:
        print(i) # a ab abc b bc c