# Reach a given score
# EasyAccuracy: 79.23%Submissions: 54K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.


class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(3,n+1):
            dp[i] += dp[i-3]
        for i in range(5,n+1):
            dp[i] += dp[i-5]
        for i in range(10,n+1):
            dp[i] += dp[i-10]
            
            
        return dp[n]
