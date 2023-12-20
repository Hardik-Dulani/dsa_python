# Modified Game of Nim
# MediumAccuracy: 57.13%

# You are given an array A of n elements. There are two players player 1 and player 2.
# A player can choose any of element from an array and remove it. 
# If the bitwise XOR of all remaining elements equals 0 after removal of the selected element, then that player loses. 
# Find out the winner if player 1 starts the game and they both play their best. 


class Solution:
    def findWinner(self, n, A):
        val = 0
        for i in range(n):
            val ^= A[i]
        return 2 if (n % 2 == 1 and val > 0) else 1
