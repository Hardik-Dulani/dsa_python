
# Buy and Sell a Share at most twice
# MediumAccuracy: 50.13%Submissions: 30K+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices. 

# Given an array price of size n, find out the maximum profit that a share trader could have made.





from typing import List


class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in price:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, p + buy2)

        return sell2
        


