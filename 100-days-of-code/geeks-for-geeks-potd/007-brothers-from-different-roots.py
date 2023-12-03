# Given two BSTs containing N1 and N2 distinct nodes respectively and given a value x, 
# your task is to complete the function countPairs(),
# that returns the count of all pairs of (a, b), where a belongs to one BST
# and b belongs to another BST, such that a + b = x.



class Solution:
    #Function to count pairs with a given sum in two BSTs.
    def countPairs(self, root1, root2, x):
        #if either of the trees is empty, return 0.
        if (root1 is None) or (root2 is None):
            return 0
        
        #using stacks to store the nodes of the trees.
        st1=[]
        st2=[]
        
        #creating dummy nodes for the top of the stacks.
        top1=Node(-1)
        top2=Node(-1)
        
        #variable to keep track of the count of pairs.
        count = 0
        
        #iterating through the trees.
        while 1:
            #traversing the left subtree of the first tree and
            #appending the nodes to stack1.
            while (root1 != None):
                st1.append(root1)
                root1 = root1.left
            
            #traversing the right subtree of the second tree and
            #appending the nodes to stack2.
            while (root2 != None):
                st2.append(root2)
                root2 = root2.right
            
            #if either of the stacks are empty, break the loop.
            if ((len(st1) == 0) or (len(st2) == 0)):
                break
            
            #getting the top nodes of both stacks.
            top1 = st1[len(st1)-1]
            top2 = st2[len(st2)-1]
            
            #checking if the sum of the top nodes is equal to x.
            if ((top1.data+top2.data) == x):
                #if yes, increment the count, remove the top nodes from both stacks,
                #and move to the right child of the top nodes.
                count = count+1
                st1.pop()
                st2.pop()
                root1 = top1.right
                root2 = top2.left
            
            #if the sum is less than x, remove the top node from stack1
            #and move to the right child of the top node.
            elif ((top1.data+top2.data)<x):
                st1.pop()
                root1 = top1.right
            
            #if the sum is greater than x, remove the top node from stack2
            #and move to the left child of the top node.
            else:
                st2.pop()
                root2 = top2.left
        
        #returning the count of pairs.
        return count
        