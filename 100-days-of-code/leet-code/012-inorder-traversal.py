# 94. Binary Tree Inorder Traversal
# Easy
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            # Traverse the left subtree
            result.extend(self.inorderTraversal(root.left))
            # Visit the root node
            result.append(root.val)
            # Traverse the right subtree
            result.extend(self.inorderTraversal(root.right))
        return result
            