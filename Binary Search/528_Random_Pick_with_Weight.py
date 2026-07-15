from random import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]

        time: O(n)
        space: O(n)
        """

        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        
        time: O(logn) for bianry search
        space: O(1)
        """

        # Normalize probability, random.random will generate num between [0.0, 1.0), times total_sum will corresponding to correct pos.
        target = (random.random()) * self.total_sum

        # binary search to find target
        l, r = 0, len(self.prefix_sums)

        while l < r:
            # to avoid Integer Overflow, 
            m = (l + r) // 2
            if target > self.prefix_sums[m]:
                l = m + 1
            # if target <= self.prefix_sum[mid], r need to -1
            # probability for target == self.prefix_sum[mid] almost near 0%, we can ignore
            else:
                r = m

        return l



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()