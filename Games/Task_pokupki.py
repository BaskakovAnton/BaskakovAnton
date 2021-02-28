print("""Здравствуйте!
Вас приветствует программа, которая сэкономит бюджет.
Для выхода из подсчетов введите -1""")

valuta = "руб."
summa = 0
count = 0
buy = 0

summa = int(input("Введите предельную сумму трат: "))
start_summa = summa

while (summa > 0 and buy != -1):
    print("Остаток: ", summa, valuta)
    buy = int(input("Введите стоимость покупки: "))

    if (buy > summa):
        print("_" * 40)
        print("Сумма товара не может быть больше суммы на покупки: ")
        print("_" * 40)
    elif (buy > 0):
        summa -= buy
        count += 1
        if (summa  < 200 and summa >0):
            print("Внимание осталось", summa, valuta + "!", "Осторожней с тратами!")
        print("*" * 20)
print("Вы потратили: ", start_summa - summa, valuta)
print("При этом совершили", count, "покупок.")
