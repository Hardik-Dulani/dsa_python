# Play With OR
# EasyAccuracy: 75.8%Submissions: 54K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are given an array arr[] of length n, you have to re-construct the same array arr[] in-place. The arr[i] after reconstruction will become arr[i] OR arr[i+1], where OR is bitwise or. If for some i, i+1 does not exists, then do not change arr[i].


class Solution:    
    def game_with_number(self, arr, n):
        # Iterating through the array till the second last element.
        for d in range(n - 1):
            # Performing bitwise OR operation on adjacent elements.
            arr[d] = arr[d] | arr[d + 1]
        
        # Returning the updated array.
        return arr