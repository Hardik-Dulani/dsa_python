# 1758. Minimum Changes To Make Alternating Binary String
# Easy

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example,
# the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

class Solution:
    def minOperations(self, s: str) -> int:
        ans1=ans2=0
        for idx,x in enumerate(s):
            if idx%2==int(x):
                ans1+=1
            else:
                ans2+=1
        return min(ans1,ans2)            
    