# String's Count
# Easy

# Given a length n, 
# count the number of strings of length n that can be made using a, b and c with at-most one b and two c allowed.

class Solution:

    def countStr(self, n):
        return (n**3 + 3 * n + 2) // 2 # code here
                
