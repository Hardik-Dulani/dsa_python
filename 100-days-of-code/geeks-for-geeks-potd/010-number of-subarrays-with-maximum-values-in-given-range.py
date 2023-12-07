# Number of subarrays with maximum values in given range
# Given an array of N elements and L and R, 
# print the number of sub-arrays such that
# the value of the maximum array element in that subarray is at least L and at most R.

class Solution:
    def countSubarrays(self, a,n,L,R): 
        ans = 0
        s = e = st = -1
        for i in range(len(a)):
            if a[i] > R:
                s = e = st = -1
            elif a[i] < L:
                if s != -1: ans += e - s + 1
                if st == -1: st = i
            else:
                if st == -1: st = i
                if s == -1: s = i
                s = min(st, max(i, s))
                e = i
                ans += i - st + 1
        return ans
