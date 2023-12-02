# Given a Binary Search Tree that contains unique positive integer values greater than 0. 
# The task is to complete the function isDeadEnd which returns true
# if the BST contains a dead end else returns false. 
# Here Dead End means a leaf node, at which no other node can be inserted.
class Solution:
    def helper(self, root, s):
        if root == None: return False
        s.add(root.data)
        left = self.helper(root.left, s)
        right = self.helper(root.right, s)
        if root.left == None and root.right == None:
            if (root.data - 1 <= 0 or root.data - 1 in s) and root.data + 1 in s:
                return True
        return left or right
    def isDeadEnd(self, root):
        return self.helper(root, set())
        # Code here