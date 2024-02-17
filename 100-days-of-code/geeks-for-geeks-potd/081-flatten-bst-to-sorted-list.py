# Flatten BST to sorted list
# MediumAccuracy: 73.7%Submissions: 10K+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are given a Binary Search Tree (BST) with n nodes, each node has a distinct value assigned to it. The goal is to flatten the tree such that, the left child of each element points to nothing (NULL), and the right child points to the next element in the sorted list of elements of the BST (look at the examples for clarity). You must accomplish this without using any extra storage, except for recursive calls, which are allowed.

# Note: If your BST does have a left child, then the system will print a -1 and will skip it, resulting in an incorrect solution.

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

import sys
sys.setrecursionlimit(10**5)
class Solution:
    def flattenBST(self, root):
        prev, head = None, root
        def dfs(node):
            nonlocal prev, head
            
            if not node:
                return
            
            dfs(node.left)
            
            if not prev:
                head = node
            else:    
                node.left = None
                prev.right = node
                
            prev = node
            dfs(node.right)
            
            return head

        return dfs(root)

