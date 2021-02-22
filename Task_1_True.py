# 1 вариант________________________________________________________________

# duration = int(input('Введите данные: '))

# days = duration // 3600 // 24
# hours = duration // 3600 - days * 24
# inutes = duration // 60 % 60
# seconds = duration % 60

# print('Дни: ', days, ',', ' часы: ', hours, ',', ' минуты: ',
# minutes, ',', ' секунды: ', seconds, '.', sep='')

# 2 вариант________________________________________________________________

# duration = int(input('Введите данные: '))
# timepiece = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]

# print(f'duration = {duration} сек\n{timepiece[0]} дн {timepiece[1]} час {timepiece[2]} мин {timepiece[3]} сек')

# 3 вариант________________________________________________________________

time_list = [60, 60, 24, 24]
word_list = [' сек', ' мин,', ' час,', ' дн,']
res_list = []

num = int(input('Введите данные: '))

for i, v in enumerate(time_list):
    res_list.append(str(num % v) + word_list[i])
    num //= v

len_list = len(res_list) - 1
while len_list >= 0:
    print(res_list[len_list], end=" ")
    len_list -= 1
