n = int(input("Введите число: "))
nums_gen = (num for num in range(1, n, 2))
print(next(nums_gen), next(nums_gen), next(nums_gen))
