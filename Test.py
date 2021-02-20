# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b , не создавая новый список.

list_numbers = []
for i in range(1, 1000):
    if i % 2 != 1:
        pass
    else:
        list_numbers.append(i ** 3)


idx = 0
list_numbers_1 = []
sum_numbers = 0

while idx < len(list_numbers):
    number = list_numbers[idx]
    str_number = str(number)
    str_number = str_number.replace('.', '')
    lst_str = list(str_number)
    lst_number = map(int, lst_str)
    s = sum(lst_number)
    if s % 7 == 0:
        sum_numbers = sum_numbers + list_numbers[idx]
    list_numbers_1.append(s)
    idx += 1

idx_1 = 0
sum_numbers_1 = 0
list_numbers_2 = []
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
    list_numbers_2.append(s_1)
    idx_1 += 1



#print(list_numbers_1)
print(sum_numbers)
#print(list_numbers_2)
print(sum_numbers_1)
