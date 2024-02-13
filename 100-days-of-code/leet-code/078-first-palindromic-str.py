# 2108. Find First Palindromic String in the Array
# Easy

# Given an array of strings words, return the first palindromic string in the array.
#  If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""