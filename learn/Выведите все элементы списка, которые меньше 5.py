# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#
# Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = (i for i in a if i < 5)
print(*result)

for i in a:
    if i < 5:
        print(i)

print(list(filter(lambda i: i < 5, a)))
