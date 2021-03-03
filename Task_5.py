
from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(n, repeat=False):
    """
    Функция возвращает случайные шутки, собранные из трех списков
    :param n: колличество шуток
    :param repeat: уникальные/неуникальные
    :return: список случайных шуток
    """

    list_of_j = []
    while n and len(nouns):
        num = randrange(len(adjectives))
        if repeat:
            list_of_j.append(f"{nouns.pop(num)} {adverbs.pop(num)} {adjectives.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return list_of_j

print(some_jokes(2))
