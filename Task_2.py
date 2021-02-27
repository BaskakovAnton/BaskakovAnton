starting_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_list = []

for i in starting_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            correct_list.append(f"'{int(i):02}'")
        else:
            correct_list.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        correct_list.append(i)

print(correct_list)
print(" ".join(correct_list))


starting_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(starting_list):
    if v.replace("+", "").replace("-", "").isdigit():
        if v.isdigit():
            starting_list[i] = f'"{int(v):02}"'
        else:
            starting_list[i] = f'"{v[0]}{int(v[1:]):02}"'

print(starting_list)
print(" ".join(starting_list))
