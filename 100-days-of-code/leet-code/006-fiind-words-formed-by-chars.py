# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for i in words: 
            count1 =0
            for j in i:
                if  not (j in chars and i.count(j) <= chars.count(j)):
                    break
                else:
                    count1+=1
            if count1==len(i):
                res+=len(i)
            
        return res