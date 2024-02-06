# Count the nodes at distance K from leaf
# MediumAccuracy: 34.27%Submissions: 45K+Points: 4
# Three 90 Challenge Extended On Popular Demand! Don't Miss Out Now 

# banner
# Given a binary tree with n nodes and a non-negative integer k, the task is to count the number of special nodes.
# A node is considered special if there exists at least one leaf in its subtree such that the distance between the node and leaf is exactly k.

# Note: Any such node should be counted only once. For example, if a node is at a distance k from 2 or more leaf nodes, then it would add only 1 to our count.

#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        #code here
        vis=set()
        self.dfs(root,[],k,vis)
        return len(vis)
    def dfs(self,root,stack,k,vis):
        if root:
            stack.append(root)
            if not root.left and not root.right:
                n=len(stack)
                if n>k and (stack[-k-1] not in vis):
                    vis.add(stack[-k-1])
            self.dfs(root.left,stack,k,vis)
            self.dfs(root.right,stack,k,vis)
            stack.pop()
