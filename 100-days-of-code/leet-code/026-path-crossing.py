from collections import defaultdict
# 1496. Path Crossing
# Easy

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
# each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, 
# if at any time you are on a location you have previously visited. Return false otherwise.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0,0]
        my_hash = defaultdict(int)
        my_hash[(0,0)] = 1
        for i in path:
            
            if i =='N':
                curr[0]+=1
            elif i =='S':
                curr[0]-=1
            elif i =='E':
                curr[1]+=1
            elif i =='W':
                curr[1]-=1
            my_hash[tuple(curr)]+=1
            
            if my_hash[tuple(curr)]>1:
                return True
        return False

