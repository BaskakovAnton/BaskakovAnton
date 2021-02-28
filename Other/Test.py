# def my_f(s_1, s_2):
# sub = s_1 - s_2
# print(f"Sub: {sub}")


# my_f(s_2=23, s_1=67)
# my_f(int(input()), int(input()))

# ____________________________________________________________________
# def my_f1(*args):
# print("Hi")
# return args


# print(my_f1(23, 68, 45, False))

# ____________________________________________________________________
# def my_f1(**kwargs):
# return kwargs


# print(my_f1(name=23, age=68, surname=45, s=False))

# ____________________________________________________________________
# my_f = lambda s_1, s_2: s_1 - s_2
# print(my_f(78, 45))

# ____________________________________________________________________
# m = 78


# def my_f():
# global n
# n = 7
# return n + m


# print(my_f())
# print(n)
# ___________________________________________________________________

#def accepted(el):
    #return el.lower().startswith('i')


#products = ['IPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
#products_sample = filter(accepted, products)
#print(type(products_sample))
#print(*products_sample)


day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
day_sales1 =[]
for idx, item in enumerate(day_sales, start=1):
    day_sales1.append(idx item)
    print('товар №', idx, '-', item)

print(day_sales1)
