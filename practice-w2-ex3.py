print ("Hello how are you?, lets calculate what can you buy:",)
budget = float(input("Enter your budget: "))
prices = [182, 415, 892, 156, 734]
stocks = ["AAPL", "MSFT", "NVDA", "META", "GOOGL"]
print("you can buy the following stocks with your budget:")
find_stocks_within_budget = [stocks[i] for i in range(len(prices)) if prices[i] <= budget]
print(find_stocks_within_budget)
affordable_stocks = len(find_stocks_within_budget)
print(f"You can buy {affordable_stocks} out of {len(stocks)} stocks within your budget.")

