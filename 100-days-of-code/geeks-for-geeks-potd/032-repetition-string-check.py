# Check if a string is repetition of its substring of k-length

# Given a string s, check if it is possible to convert it into a string that is the repetition of a substring of length k. 
# Conversion has to be done by following the steps mentioned below only once:

# 1. Select two indices i and j (zero-based indexing, i could be equal to j), such that i and j are divisible by k.
# 2. Select substrings of length k starting from indices i and j.
# 3. Replace substring starting at index i with substring starting at index j within the string.


class Solution:
    def kSubstrConcat(self, n, s, k):
        h={}
        if n%k!=0:
            return 0
        c=0
        for i in range(0,n-k+1,c+k):
            r=s[i:i+k]
          #  print(r)
            c+=1
            h[r]=h.get(r,0)+1
            if len(h)>2:
                return 0
        ans=0   
        if len(h)==2 and n//k==2:
            return 1
        for i in h:
            if ans==0 and h[i]>1:
                ans=1
            elif ans==1 and h[i]>1:
                ans=0
                return 0
        return ans