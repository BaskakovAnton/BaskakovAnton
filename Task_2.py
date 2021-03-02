def num_translate():
    for i in dic_word:
        if userword == i:
            return (dic_word.get(i))
        elif userword != i:
            if userword.lower() == i:
                return (dic_word.get(i).capitalize())


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

userword = input('Введите значение: ')
answer = num_translate()
print(answer)
