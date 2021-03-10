def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num

nums_gen = nums_generator(int(input("Введите число: ")))

print(*nums_gen, sep=", ")
