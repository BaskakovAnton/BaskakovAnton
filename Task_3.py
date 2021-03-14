# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.


from itertools import zip_longest

users = open("users.csv", "r", encoding="utf-8")
for line in users:
    users_list = line.split()
    for i in users_list:
        i = i.replace(',', ' ')
        print(i)

hobby = open("hobby.csv", "r", encoding="utf-8")
for line in hobby:
    print(line, end="")

#rez = zip_longest(users, hobby, fillvalue=None)
#print(*rez)

# with open("users.csv", "r", encoding="utf-8") as users:
#     users_list = ((line.replace(',', ' ')) for line in users)
#     print(*users_list)
#
# with open("hobby.csv", "r", encoding="utf-8") as hobby:
#     hobby_list = ((line.replace(',', ' ')) for line in hobby)
#     original_hobby = hobby_list
#     print(*hobby_list)


users.close()
hobby.close()
