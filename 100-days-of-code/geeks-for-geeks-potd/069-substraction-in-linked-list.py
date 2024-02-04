
# Subtraction in Linked List
# HardAccuracy: 12.94%
# You are given two linked lists that represent two large positive numbers. 
# From the two numbers represented by the linked lists, subtract the smaller number from the larger one. 
# Look at the examples to get a better understanding of the task.



class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        num1 = num2 = ''
        while l1:
            num1+=str(l1.data)
            l1 = l1.next
        while l2:
            num2+=str(l2.data)
            l2 = l2.next
        ans =  str(abs(int(num1)-int(num2)))
        
        n = Node(ans[0])
        head = n
        for i in ans[1:]:
            temp = Node(i)
            head.next = temp
            head = temp
        return n
