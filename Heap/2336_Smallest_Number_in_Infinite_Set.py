import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        # for search num whether should addback in O(1)
        self.added_set = set()
        # min_heap to store add back nums
        self.heap = []
        # recored untouched number 
        self.curr = 1

    def popSmallest(self):
        """
        :rtype: int

        time: O(logm), m is size for set and heap
        space: O(m)
        """
        if self.heap:
            ans = heapq.heappop(self.heap)
            # also need remove from added_set
            self.added_set.remove(ans)
        # if heap is empty, directly remove
        else:
            ans = self.curr
            self.curr += 1
        
        return ans

    def addBack(self, num):
        """
        :type num: int
        :rtype: None

        time: O(logm), m is size for set and heap
        space: O(m)
        """
        # if num >= curr, means number still in infinite set, just return
        # if num in added_set(search in O(1)), also return
        if num >= self.curr or num in self.added_set:
            return
        # othewise add to heap and added_set
        heapq.heappush(self.heap, num)
        self.added_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)