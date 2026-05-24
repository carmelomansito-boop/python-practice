def calculation_gain_percentage(cost_price, selling_price):
    gain = selling_price - cost_price
    gain_percentage = (gain / cost_price) * 100
    return gain_percentage  
result = calculation_gain_percentage(100, 150)
print("Gain percentage:", result)