# Sum of leaf nodes in BST
# EasyAccuracy: 70.36%Submissions: 39K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# Given a Binary Search Tree with n nodes, find the sum of all leaf nodes. BST has the following property (duplicate nodes are possible):

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node’s key.
# Your task is to determine the total sum of the values of the leaf nodes.

# Note: Input array arr doesn't represent the actual BST, it represents the order in which the elements will be added into the BST.
class TreeNode:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def sumOfLeafNodes(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return root.data
        
        return self.sumOfLeafNodes(root.left) + self.sumOfLeafNodes(root.right)