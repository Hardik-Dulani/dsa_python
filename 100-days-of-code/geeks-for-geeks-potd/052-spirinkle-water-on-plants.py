# Water the plants
# MediumAccuracy: 61.04%


# A gallery with plants is divided into n parts, numbered 0, 1, 2, 3, ..., n-1. 
# There are provisions for attaching water sprinklers in every division.
#  A sprinkler with range x at division i can water all divisions from i-x to i+x.

# Given an array gallery[] consisting of n integers, 
# where gallery[i] is the range of the sprinkler at partition i (a power of -1 indicates no sprinkler attached), 
# return the minimum number of sprinklers that need to be turned on to water the entire gallery. 
# If there is no possible way to water the full length using the given sprinklers, print -1.




class Solution:
    def min_sprinklers(self, gallery, n):
        intervals = sorted([(i-g, i+g) for i, g in enumerate(gallery) if g != -1], reverse=True)
        reachable, best, res = 0, 0, 0
     
        while reachable < n:
            if intervals and intervals[-1][0] <= reachable:
                s, e = intervals.pop()
                best = max(best, e+1)
            elif best > reachable:
                reachable = best
                res += 1
            else:
                return -1
        return res


