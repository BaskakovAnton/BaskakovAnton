a = int(input())
b = int(input())
c = int(input())
d = int(input())

for h in range(c, d + 1):
    print('\t' + str(h), end='')
print(end='\n')
for i in range(a, b + 1):
    print(str(i) + '\t', end='')
    for j in range(c, d + 1):
        print(str(i * j), end='\t')
    print(end='\n')




# #Ввод данных
# a = 7
# b = 10
# c = 5
# d = 6
# #начало Цикла
# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i * j),end='\t')# выводим результат умножения соответствующих чисел в таблицу
#     print(end='\n')