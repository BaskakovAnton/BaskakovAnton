# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы

def thesaurus(*args):
    dict_names = {}
    for i in sorted(args):
        letter = i[0]
        if letter in dict_names:
            dict_names[letter] += [i]
        else:
            dict_names[letter] = [i]

    return dict_names

print(thesaurus("Иван", "Антон", "Андрей", "Илья", "Виктория", "Игнат", "Владимир"))