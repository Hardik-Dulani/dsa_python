# Does array represent Heap
# EasyAccuracy: 30.97%Submissions: 48K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.


class Solution:
    def isMaxHeap(self, arr, n):
        # Start from the parent of the last node and move up to the root
        for i in range((n // 2) - 1, -1, -1):
            # If the current node is smaller than its left child or right child (if exists)
            if arr[i] < arr[2*i + 1] or (2*i + 2 < n and arr[i] < arr[2*i + 2]):
                return False
        return True           


