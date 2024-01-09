# 872. Leaf-Similar Trees
# Easy

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2