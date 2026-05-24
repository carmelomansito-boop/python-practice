stocks = ["AAPL", "MSFT", "GOOGL", "NVDA", "META"]
prices = [182.50, 415.20, 175.80, 900.10, 515.30]
for s, p in zip(stocks, prices):
    print(f"{s}, ${p}")
highest_price = 0
for stock, price in zip(stocks, prices):
    if price > highest_price:
        highest_price = price
        highest_stock = stock
print(f"The highest priced stock is {highest_stock} at ${highest_price}")
total = f"${sum(prices):.2f}"
print(f"The total cost of all the stocks is: {total}")