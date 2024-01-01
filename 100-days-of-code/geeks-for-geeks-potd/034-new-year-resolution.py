# New Year Resolution

# As the clock struck midnight on New Year's Eve, 
# Geek bid farewell to the wasted moments of 2023, 
# realizing the untapped potential of GFG's Problem of the Day.

# His 2024 resolution: Solve POTD every day.

# Eager to earn coins for GFG Merchandise, Geek faces new rules:

# Earning Coin: Geek can accumulate coins[i] by solving the POTD on the ith day, where 1 <= coins[i] <= 2024 and the sum of coins <= 2024.
# Merchandise Eligibility: To purchase merchandise, the coins earned must be divisible by 20 or 24, or precisely equal to 2024.
# Geek's resolutions often fades over time. Realistically, he can only commit to active participation for N (where N ≤ 366) days.
# Given the value of N and number of coins associated with each POTD, 
# can Geek strategically solve some (or all) POTDs to become eligible for redeeming merchandise?


from typing import List


class Solution:
    def isPossible(self, n : int, arr : List[int]) -> bool:
        # code here
        dp = [[0]*(n+1) for _ in range(2025)]
        
        for i in range(n+1):
            dp[0][i] = True
            
        for s in range(1, 2025):
            for i in range(n):
                dp[s][i+1] = dp[s][i]
                if s >= arr[i]:
                    dp[s][i+1] = dp[s][i+1] or dp[s-arr[i]][i]
                if dp[s][i+1] and (s%20 == 0 or s%24 == 0 or s == 2024):
                    return True
        
        return False