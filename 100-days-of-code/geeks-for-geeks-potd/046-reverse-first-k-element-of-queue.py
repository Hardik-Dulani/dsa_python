# Reverse First K elements of Queue
# EasyAccuracy: 81.28%
# Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, 
# leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.
# Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.



#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        return q[:k][::-1]+q[k:]

