# Given an array arr of size N, determine whether this array represents an inorder traversal of a BST. 

# Note: All keys in BST must be unique.
class Solution:
    def isRepresentingBST(self, arr, N):
        for i in range(1,N):
            if arr[i] < arr[i-1]:
                return 0
        return 1