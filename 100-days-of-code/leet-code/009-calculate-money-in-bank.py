# 1716.

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
# he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        weeks = n//7
        days = n%7
        for i in range(1,weeks+1):
            s = sum(range(i,i+7))
            ans+= s
            print(ans,i,weeks)
        print(weeks,days)
        ans+= sum(range(weeks+1,weeks+days+1))
        return ans

            
        
