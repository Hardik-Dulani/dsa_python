# 1637. Widest Vertical Area Between Two Points Containing No Points
# Medium

# Given n points on a 2D plane where points[i] = [xi, yi], 
# Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
# The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ys = [a[0] for a in points]
        ys =  sorted(ys)
        diff = 0
        
        for i in range(1,len(ys)):
            diff = max(diff,ys[i]-ys[i-1])
        return diff
        