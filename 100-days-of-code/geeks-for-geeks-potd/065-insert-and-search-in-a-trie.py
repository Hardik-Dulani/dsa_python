# Insert and Search in a Trie
# MediumAccuracy: 65.68%
# Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
# Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.
# Note: To test the correctness of your code, the code-judge will be inserting a list of N strings called into the Trie,
# and then will search for the string key in the Trie. The code-judge will generate 1 if the key is present in the Trie, else 0.

#User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""
class Solution:
    def insert(self, root, key):
        #code here
        for k in key:
            ind=ord(k)-ord('a')
            if not root.children[ind]:
                root.children[ind]=TrieNode()
            root=root.children[ind]
        root.isEndOfWord=True
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        #code here
        for k in key:
            ind=ord(k)-ord('a')
            if not root.children[ind]:
                return False
            root=root.children[ind]
        return root.isEndOfWord