# Power Set
# MediumAccuracy: 43.3%Submissions: 82K+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# Given a string s of length n, find all the possible subsequences of the string s in lexicographically-sorted order.
#User function Template for python3

class Solution:
    def generate_subsequences(self, s, index, current, result):
        if index == len(s):
            if current:
                result.append(''.join(current))
            return

        # Include the current character
        self.generate_subsequences(s, index + 1, current + [s[index]], result)

        # Exclude the current character
        self.generate_subsequences(s, index + 1, current, result)
        
    def AllPossibleStrings(self, s):
        # Code here
        result = []
        self.generate_subsequences(s, 0, [], result)
        return sorted(result)


