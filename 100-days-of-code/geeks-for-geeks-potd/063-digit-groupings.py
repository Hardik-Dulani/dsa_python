# Count digit groupings of a number
# MediumAccuracy: 59.38%
# Given a string str consisting of digits, you can divide it into sub-groups by separating the string into substrings. 
# For example, "112" can be divided as {"1", "1", "2"}, {"11", "2"}, {"1", "12"}, and {"112"}.

# A valid grouping can be done if you are able to divide sub-groups where the sum of digits in a sub-group is 
# less than or equal to the sum of the digits of the sub-group immediately right to it. 
# Your task is to determine the total number of valid groupings that could be done for a given string.


class Solution:
    def TotalCount(self, s):
        pfs=[int(x) for x in s]
        for i,v in enumerate(pfs):
            if i>=1:
                pfs[i]+=pfs[i-1]
        m=len(pfs)
        from functools import lru_cache
        @lru_cache(None)
        def dp(cur=0,sm=0):
            nonlocal pfs,m
            ans=0
            prv=pfs[cur-1] if cur-1>=0 else 0
            for nxt in range(cur,m):
                left=pfs[nxt]-prv
                right=pfs[m-1]-pfs[nxt]
                if sm<=left<=right:
                    ans+=1+dp(nxt+1,left)
            return ans
        return dp()+1