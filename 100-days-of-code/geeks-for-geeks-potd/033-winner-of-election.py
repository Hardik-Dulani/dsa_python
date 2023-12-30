# Winner of an election
# EasyAccuracy: 53.75%


# Given an array of n names arr of candidates in an election, 
# where each name is a string of lowercase characters. A candidate name in the array represents a vote casted to the candidate. 
# Print the name of the candidate that received the maximum count of votes. 
# If there is a draw between two candidates, then print lexicographically smaller name.

#User function Template for python3
from collections import Counter
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        word_counter = Counter(arr)
      
        # # Get the words with the maximum count
        max_words = word_counter.most_common()
        
        # # Find the maximum count
        max_count = max_words[0][1]
        
        # # Get the lexicographically smallest word with the maximum count
        max_word = min(word for word, count in max_words if count == max_count)
        return max_word, max_count