# Check if all leaves are at same level
# EasyAccuracy: 39.47%
# Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. 
# Return true if all leaf nodes are at the same level, and false otherwise.

#User function Template for python3
class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    leafLevel = 0
    def Check_Ok(self,root,level):
        
        if not root:
            return True
        if not root.right and not root.left:
            global leafLevel
            
            if leafLevel==0:
                leafLevel = level
                return True
            return (leafLevel==level)
        return self.Check_Ok(root.left,level+1) and self.Check_Ok(root.right,level+1)
            
    def check(self, root):
        #Code here
        global leafLevel
        leafLevel = 0
        return self.Check_Ok(root,0)

