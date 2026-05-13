from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        time: O(n)
        space: O(k), max size for deque is k
        """
        # dq store idx to maintain size of k window
        dq = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            # remove last nums from deque which is smaller than curr num
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            # add curr num to deque
            dq.append(r)
            
            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
            
            # out of size of window, move head
            if dq[0] < l: 
                dq.popleft()

        return res