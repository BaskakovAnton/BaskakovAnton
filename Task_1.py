# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи.


def num_translate():
    for i in dic_word:
        if user_word == i:  # проверяю словарь на совпадение вводимого значения с ключами словаря
            return dic_word.get(i)  # при совпадении вывожу значение


dic_word = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

user_word = input('Введите значение: ')
answer = num_translate()
print(num_translate())
