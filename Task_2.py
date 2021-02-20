list_numbers = []
for i in range(1, 1000):
    if i % 2 != 1:
        pass
    else:
        list_numbers.append(i ** 3)

result_a = 0
result_b = 0

for idx in range(len(list_numbers)):
    num = list_numbers[idx]
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum % 7 == 0:
        result_a += list_numbers[idx]

for idx in range(len(list_numbers)):
    num = list_numbers[idx] + 17
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    if digit_sum % 7 == 0:
        result_b += list_numbers[idx]

print('Сумма чисел №1: ', result_a, 'Правильный ответ: 17485588610')
print('Сумма чисел №2: ', result_b, 'Правильный ответ: 15392909930')
