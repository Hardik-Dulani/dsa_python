# Distribute candies in a binary tree
# HardAccuracy: 67.53%
# Given a binary tree with N nodes, in which each node value represents number of candies present at that node. 
# In one move, one may choose two adjacent nodes and move only one candy from one node to another (the move may be from parent to child, 
# or from child to parent.) 
# The task is to find the number of moves required such that every node has exactly one candy.
# Note that the testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy,
# after some moves.



'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def distributeCandy(self, root):
        self.moves = 0
        def dfs(root):
            if not root:
                return 0
                
            left_requires = dfs(root.left)
            right_requires = dfs(root.right)
            
            self.moves += abs(left_requires) + abs(right_requires)
            remaining_coins = left_requires + right_requires + root.data - 1
            
            return remaining_coins  
        dfs(root)
        return self.moves

