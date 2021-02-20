res = []
summ = 0

for i in range(1, 1000, 2):
    buf = str(i ** 3)
    char: str
    for char in buf:
        summ = summ + int(char)
    if summ % 7 == 0:
        res.append(summ)

print(res)

res = []
summa = 0

for i in res:
    summa = summa + int(i)
    summa += i

print(summa)
