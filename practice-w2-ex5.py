stocks = ["AAPL", "MSFT", "NVDA", "META", "GOOGL"]
prices = [182, 415, 892, 156, 174]
for s, p in zip(stocks, prices):
    print(f"{s}, {p}")
budget = int(input("Enter your budget: "))
total = 0 
for stock, price in zip(stocks, prices):
    if price <= budget:
        print(f"You can buy {stock} at ${price}")
        total += price
print(f"The total cost of the stocks you can buy is: ${total}")
