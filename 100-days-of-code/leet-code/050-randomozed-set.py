# 380. Insert Delete GetRandom O(1)
# Solved
# Medium

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.


class RandomizedSet:

    def __init__(self):
        self.random_set = set()

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        else:
            self.random_set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        list1 = list(self.random_set)
        return random.choice(list1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()