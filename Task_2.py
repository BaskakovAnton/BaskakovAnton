import operator
from collections import Counter

with open("nginx_logs.txt", "r", encoding="utf-8") as parsing:
    content = ((line.split()[0]) for line in parsing)
    content = Counter(content)
    spamer = max(content.items(), key=operator.itemgetter(1))
    print("Спамер: ", spamer)
