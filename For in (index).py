day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]

total_sales = 0

for product_price in day_sales:
    total_sales += product_price

price_per_product = total_sales / len(day_sales)
print(price_per_product)
