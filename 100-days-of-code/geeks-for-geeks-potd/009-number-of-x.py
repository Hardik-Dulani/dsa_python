# Given two integers L, R, and digit X. 
# Find the number of occurrences of X in all the numbers in the range (L, R) excluding L and R.
class Solution:    
    def countX(self,L,R,X):
        X=str(X)
        ans=0
        for i in range(L+1,R):
            i=str(i)
            ans+=i.count(X)
        return ans