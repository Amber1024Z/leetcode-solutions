import heapq
class MedianFinder(object):
    """
    time: O(logn) for addNum, O(1) for findMedian
    space: O(n), we need to store all the numbers in the data stream."""

    def __init__(self):
        # small: Max heap, storing the [smaller] half of the array 
        # large: Min heap, storing the [larger] half of the array 
        # Always ensures that len(small) >= len(large)
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # push num to small first
        heapq.heappush(self.small, -num)
        val = -heapq.heappop(self.small)
        # push to large heap
        heapq.heappush(self.large, val)

        # make sure len(large) <= len(samll)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        # if length is odd, median is heap of small
        n = len(self.small) + len(self.large)
        if n % 2 != 0:
            return float(-self.small[0])
        else:
            return float((-self.small[0] + self.large[0]) / 2.0)

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()