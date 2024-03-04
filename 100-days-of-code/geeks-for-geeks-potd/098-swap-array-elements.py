# Swap the array elements
# EasyAccuracy: 64.61%Submissions: 72K+Points: 2
# Internship Alert!
# New month-> Fresh Chance to top the leaderboard and get SDE Internship! 

# banner
# Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.

#User function Template for python3

class Solution:
	def swapElements(self, arr, n):
	    for i in range(n-2):
	        
	        arr[i],arr[i+2] = arr[i+2],arr[i]
	    return arr
