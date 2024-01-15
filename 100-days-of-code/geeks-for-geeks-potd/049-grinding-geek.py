# Grinding Geek
# MediumAccuracy: 50.0%

# GeeksforGeeks has introduced a special offer where you can enroll in any course, 
# and if you manage to complete 90% of the course within 90 days, you will receive a refund of 90%.

# Geek was fascinated by this offer. This offer was valid for only n days, 
# and each day a new course was available for purchase. Geek decided that if he bought a course on some day,
# he will complete that course on the same day itself and redeem floor[90% of cost of the course] amount back. 
# Find the maximum number of courses that Geek can complete in those n days if he had total amount initially.

# Note: On any day, Geek can only buy the new course that was made available for purchase that day.
    



from typing import List

class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        dp = [[-1] * (total + 1) for _ in range(n + 1)]
        
        def help(ind, total):
            nonlocal n, cost, dp
            
            if ind == n:
                return 0
            
            if dp[ind][total] != -1:
                return dp[ind][total]
            
            if total < cost[ind]:
                dp[ind][total] = help(ind + 1, total)
                return dp[ind][total]
            
            left_amount = total - cost[ind]
            refund = int(cost[ind] * 0.9)
            left_amount += refund
            
            pick = 1 + help(ind + 1, left_amount) 
            not_pick = help(ind + 1, total)  
            
            dp[ind][total] = max(pick, not_pick)
            return dp[ind][total]

        return help(0, total)
        

