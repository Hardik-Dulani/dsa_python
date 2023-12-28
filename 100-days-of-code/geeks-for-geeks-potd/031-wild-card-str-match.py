# Wildcard string matching
# HardAccuracy: 23.88%


# Given two strings wild and pattern. Determine if the given two strings can be matched given that, 
# wild string may contain * and ? but string pattern will not. * and ? can be converted to another character according to the following rules:

# * --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
# ? --> This character in string wild can be replaced by any one character.


#User function Template for python3

import fnmatch
class Solution:
    def match(self, wild, pattern):
        # code here
        return fnmatch.fnmatch(pattern,wild)
