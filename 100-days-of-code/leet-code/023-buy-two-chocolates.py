# 2706. Buy Two Chocolates
# Easy

# You are given an integer array prices representing the prices of various chocolates in a store. 
# You are also given a single integer money, which represents your initial amount of money.

# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. 
# You would like to minimize the sum of the prices of the two chocolates you buy.

# Return the amount of money you will have leftover after buying the two chocolates. 
# If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min = float('inf')
        second_min = float('inf')
        for i in range(len(prices)):
            if prices[i] <= first_min:
                first_min,second_min = prices[i],first_min
            elif prices[i]<second_min:
                second_min = prices[i]
        left = money - first_min - second_min
        if left>=0:
            return left
        return money 

        