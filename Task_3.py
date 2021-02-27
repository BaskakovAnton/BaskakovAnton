starting_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(starting_list):
    if v.replace("+", "").replace("-", "").isdigit():
        if v.isdigit():
            starting_list[i] = f'"{int(v):02}"'
        else:
            starting_list[i] = f'"{v[0]}{int(v[1:]):02}"'

print(starting_list)
print(" ".join(starting_list))
