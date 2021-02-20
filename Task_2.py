list_numbers = []
for i in range(1, 1000):
    if i % 2 != 1:
        pass
    else:
        list_numbers.append(i ** 3)

idx = 0
sum_numbers = 0

while idx < len(list_numbers):
    number = list_numbers[idx]
    str_number = str(number)
    str_number = str_number.replace('.', '')
    lst_str = list(str_number)
    lst_number = map(int, lst_str)
    s = sum(lst_number)
    if s % 7 == 0:
        sum_numbers = sum_numbers + s
    idx += 1

idx_1 = 0
sum_numbers_1 = 0

while idx_1 < len(list_numbers):
    number_1 = list_numbers[idx_1]
    s_2 = list_numbers[idx_1] + 17
    str_number = str(s_2)
    str_number = str_number.replace('.', '')
    lst_str = list(str_number)
    lst_number = map(int, lst_str)
    s_1 = sum(lst_number)
    if s_1 % 7 == 0:
        sum_numbers_1 = sum_numbers_1 + s_1
    idx_1 += 1

print('Cписок кубов: ', list_numbers)
print('Сумма №1: ', sum_numbers)
print('Сумма №2: ', sum_numbers_1)
