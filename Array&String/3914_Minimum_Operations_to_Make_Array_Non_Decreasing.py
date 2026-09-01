class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """

        # target is to make array non-decreasing, nums[0] <= nums[1] <= nums[2] <= nums[3]

        ans = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                ans += nums[i - 1] - nums[i]

        return ans
