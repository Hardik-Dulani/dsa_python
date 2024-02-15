# Count all Possible Path
# MediumAccuracy: 53.34%Submissions: 14K+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are presented with an undirected connected graph consisting of n vertices and connections between them represented by an adjacency matrix. Your objective is to determine whether it is possible to start traversing from a node, x, and return to it after traversing all the vertices at least once, using each edge exactly once.

#User function Template for python3

class Solution:
    def isPossible(self, paths):
        # Code here
        for i in paths:
            if i.count(1)%2:
                return 0
        return 1
