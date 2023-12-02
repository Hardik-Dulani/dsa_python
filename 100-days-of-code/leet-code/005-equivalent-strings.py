# Given two string arrays word1 and word2, 
# return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        string1 = ""
        string2 = ""
        for i in word1:
            string1+=i
        for i in word2:
            string2+=i
        if string1==string2:
            return True
        return False