# 1457. Pseudo-Palindromic Paths in a Binary Tree
# Medium

# Given a binary tree where node values are digits from 1 to 9. 
# A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

class Solution:
    def pseudoPalindromicPaths(self, root):
        count = 0
        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()

            if node:
                path ^= 1 << node.val

                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count

