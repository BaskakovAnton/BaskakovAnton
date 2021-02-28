#summ = 0
#for i in range(3):
  #  a = int(input("Введите число: "))
   # summ += a

#print(summ)


# факториал
fact = 1
x =int(input("Введите число (x!): "))

for i in range(2, x + 1):
    fact *= i

print(str(x) + "! =", fact)
