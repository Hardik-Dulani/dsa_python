
# Buy Maximum Stocks if i stocks can be bought on i-th day

# In a stock market, there is a product with its infinite stocks. 
# The stock prices are given for N days, where price[i] denotes the price of the stock on the ith day.
# There is a rule that a customer can buy at most i stock on the ith day.
# If the customer has an amount of k amount of money initially. The task is to find out the maximum number of stocks a customer can buy. 


from typing import List

class Solution:
    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
        arr = ((price[i], i+1) for i in range(n))
        arr = sorted(arr, key=lambda x: x[0])
        res = 0
        for today, stocks in arr:
            can_buy = min(stocks, k // today)
            res += can_buy
            k -= today * can_buy
        return res
