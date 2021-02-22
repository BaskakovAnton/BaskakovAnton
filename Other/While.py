day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]

idx = 0
total_sales = 0

while idx < len(day_sales):
    total_sales = total_sales + day_sales[idx]
    idx += 1

price_per_product = total_sales / len(day_sales)
print(price_per_product)