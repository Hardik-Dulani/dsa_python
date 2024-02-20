# Word Break
# MediumAccuracy: 40.86%Submissions: 94K+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# Given a string s and a dictionary of n words dictionary, find out if a s can be segmented into a space-separated sequence of dictionary words. Return 1 if it is possible to break the s into a sequence of dictionary words, else return 0. 

# Note: From the dictionary dictionary each word can be taken any number of times and in any order.


#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
    
        # create a dictionary to store words from the dictionary list
        dic = {}
    
        # iterate through the words in the dictionary list
        for i in  dictionary:
    
            # check if the word exists in the input s
            if i in s:
    
                # if the first letter of the word exists in the dictionary 
                # dictionary, append the word to the list associated with 
                # that letter; otherwise, create a new list with the word
                if i[0] in dic:
                    dic[i[0]].append(i)
                else:
                    dic[i[0]]=[i]
        
        # define a recursive function to solve the word break problem
        def solve(st, k,  dp):
    
            # base case: if the entire string is broken
            if len(st)==k:
                return True
            
            # if the current substring has already been processed,
            # return its corresponding result
            elif  dp[k]!=None:
                return  dp[k]
            
            # if the current character has associated words in the dictionary
            elif st[k] in dic:
    
                # iterate through the words associated with the current 
                # character in the dictionary
                for i in dic[st[k]]:
    
                    # check if the length of the word is smaller or equal 
                    # to the remaining substring
                    if len(i)<=len(st[k:]):
    
                        # check if the word matches the current substring
                        if st[k:k+len(i)]==i:
    
                            # increment k by the length of the matched word
                            k+=len(i)
                            
                            # recursively call the solve function with the 
                            # updated substring
                            rt = solve(st,k, dp)
    
                            # if the recursive call returns True, update 
                            # the corresponding result and return True
                            if rt:
                                dp[k]=True
                                return True
                            else:
    
                                # if the recursive call returns False, 
                                # decrement k by the length of the matched 
                                # word to backtrack
                                k=k-len(i)
    
                # if none of the words match the current substring, update 
                # the result to False and return False
                dp[k]=False
                return False     
            else:
    
                # if the current character does not have associated words 
                # in the dictionary, update the result to False and return False
                dp[k]=False
                return False
    
        # initialize a list to store the results of the solve function 
        dp=[None]*(len(s)+1)
    
        # set the initial value of k to 0
        k=0
    
        # call the solve function to check if it is possible to break the string
        res = solve(s, k,  dp)
    
        # return the final result
        return res