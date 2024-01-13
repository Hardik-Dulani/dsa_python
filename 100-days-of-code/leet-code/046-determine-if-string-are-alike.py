# 1704. Determine if String Halves Are Alike
# Solved
# Easy

# You are given a string s of even length. Split this string into two halves of equal lengths, and 
# let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
# Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)//2
        s1 = s[:l].lower()
        s2 = s[l:].lower()
        c1 = 0
        c2 = 0
        for i,j in zip(s1,s2):
            if i in "aeiou":
                c1+=1
            if j in "aeiou":
                c2+=1
        return c1==c2
                


