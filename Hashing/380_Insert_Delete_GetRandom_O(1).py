import random
class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool

        Returns true if the set did not already contain the specified element.
        time: O(1) for insert
        """
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool

        Returns true if the set contained the specified element.
        time: O(1) for remove since we swap the target element with the last element and pop the last element, 
        we don't need to shift elements after remove
        """
        if val in self.dict:
            # get the last element of list
            last_element = self.list[-1]
            # get idx of element we wish to remove
            idx = self.dict[val]

            # swap value, target element and last
            self.list[idx] = last_element
            self.dict[last_element] = idx

            # remove the last element we swap
            self.list.pop()
            del self.dict[val]
            
            return True

        return False

    def getRandom(self):
        """
        :rtype: int
        """
        
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()