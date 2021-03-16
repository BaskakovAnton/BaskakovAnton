with open("nginx_logs.txt", "r", encoding="utf-8") as parsing:
    for line in parsing:
        content = line.split()[0], line.split()[5][1:], line.split()[6]
        for i in content:
            print(i)


with open("nginx_logs.txt", "r", encoding="utf-8") as parsing:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in parsing)
    for i in content:
        print(i)
