prices = [182, 415, 892, 156, 734]
stocks = ["AAPL", "MSFT", "NVDA", "META", "GOOGL"]
print([stock for stock, price in zip(stocks, prices) if price > 200])
highest_price = -1
for price in prices: 
    if price > highest_price:
        highest_price = price
print(highest_price)
