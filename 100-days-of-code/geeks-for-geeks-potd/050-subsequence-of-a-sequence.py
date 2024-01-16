
# Sequence of Sequence
# MediumAccuracy: 61.93%

# Given two integers m and n, try making a special sequence of numbers seq of length n such that

# seqi+1 >= 2*seqi 
# seqi > 0
# seqi <= m
# Your task is to determine total number of such special sequences possible.


#User function Template for python3

class Solution:
    def numberSequence(self, m, n):
        # code here
        if m<n:
            return 0;

        if n==0:
            return 1;
        return self.numberSequence(m/2,n-1)+self.numberSequence(m-1,n);
