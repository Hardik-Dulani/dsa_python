# Paths from root with a specified sum
# MediumAccuracy: 55.0%
# Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto the given sum. Path may not end on a leaf node.


#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def printPaths(self, root, sum):
        given_sum = sum
        res = []
        def dfs(root, path, total):
            if root:
                if root.data + total == given_sum:
                    res.append(path + [root.data])
                dfs(root.left, path+[root.data], root.data+total)
                dfs(root.right, path+[root.data], root.data+total)
            return
        
        path = []
        dfs(root, path, 0)
        return res