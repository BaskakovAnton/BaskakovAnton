# 1 вариант _________________________________________________________

# Инициализируем переменные
list_of_cubes = []
add_list_of_cubes = []
all_sum = 0

# заполняем список значениями в диапозоне от 1 до 1000
# с шагом 2 - нечетные значения
# 1 + 2 = 3
# 3 + 2 = 5
# и т.д

# каждый элемент возводим в куб при добавлении в список
for i in range(1, 1001, 2):
    list_of_cubes.append(i ** 3)

# перебираем элементы списка
for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10 # отрезаем последнюю цифру
        val //= 10 # удаляем поспоследнюю цифру
    if sum_digits % 7 == 0: # фильтр на кратность 7
        all_sum += list_of_cubes[ind]

print(all_sum)

for m in list_of_cubes:
    add_list_of_cubes.append(m + 17)

# обнуляем значение перепенной для повторного использования
all_sum = 0

for ind, val in enumerate(add_list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind] + 17

print(all_sum)

# 2 вариант _________________________________________________________

list_of_cubes = []
all_sum = 0

for i in range(1, 1001, 2):
    list_of_cubes.append(i ** 3)

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]
    list_of_cubes[ind] += 17

print(all_sum)

all_sum = 0

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]

print(all_sum)