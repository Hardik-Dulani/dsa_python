# Panagram Checking
# EasyAccuracy: 61.34%

# Given a string s check if it is "Panagram" or not.

# A "Panagram" is a sentence containing every letter in the English Alphabet.



#from collections import Counter
class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        s = s.lower()
        # dic = Counter(s)
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        
        cnt = 0
        for k,v in dic.items():
            if 97 <= ord(k) <= 122:
                cnt+=1
                
        if cnt == 26:
            return 1
        else:
            return 0
                
            