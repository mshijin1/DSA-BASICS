def stock_buy_and_sell(prices):
    n=len(prices)
    min_price=prices[0]
    max_profit=0
    
    for i in range(1, n):
        if prices[i]<min_price:
            min_price=prices[i]
        else:
            max_profit=max(max_profit, prices[i]-min_price)
            day=i
    return max_profit, i


prices=[7, 1, 5, 3, 6, 4]
max_profit, i=stock_buy_and_sell(prices)
print("Max_profit: ", max_profit, " " , "Day: ",i)