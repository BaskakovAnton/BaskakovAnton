duration = int(input('Введите данные: '))

m = duration // 60
s = duration % 60
h = duration // 3600
m_1 = (duration % 3600) // 60
s_1 = (duration % 3600) % 60
d = duration // 86400
h_2 = (duration % 86400) // 3600
m_2 = ((duration % 86400) % 3600) // 60
s_2 = ((duration % 86400) % 3600) % 60

if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(m, 'мин', s, 'сек')
elif 3600 <= duration < 86400:
    print(h, 'час', m_1, 'мин', s_1, 'сек')
else:
    print(d, 'дн', h_2, 'час', m_2, 'мин', s_2, 'сек')
