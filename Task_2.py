
import operator
from collections import Counter

with open("nginx_logs.txt", "r", encoding="utf-8") as parsing:
    content = ((line.split()[0]) for line in parsing)
    content = Counter(content)
    spammer = max(content.items(), key=operator.itemgetter(1))[0]
    spammer_request = max(content.items(), key=operator.itemgetter(1))[1]
    print("Спамер: ", spammer, "Количество запросов: ", spammer_request)
