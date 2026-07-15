class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        
        curr = 0
        ans = 0

        for num in nums:
            if num == 1:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0

        return ans