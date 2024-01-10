# Longest subarray with sum divisible by K
# MediumAccuracy: 33.72%


# Given an array arr containing N integers and a positive integer K, 
# find the length of the longest sub array with sum of the elements divisible by the given value K.


class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) :
        dct = {0: -1}
        res = sm = 0
        for i, num in enumerate(arr):
            sm += num
            sm_rem = sm % K
            if sm_rem < 0:
                sm_rem += K
            if sm_rem in dct:
                res = max(res, i - dct[sm_rem])
            else:
                dct[sm_rem] = i
        return res


