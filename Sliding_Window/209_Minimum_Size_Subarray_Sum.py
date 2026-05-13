class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: 0(1)
        """

        ans = float('inf')
        l = 0

        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            # only shrink when curr_sum >= target
            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                # remove leftmost num and move left +1
                curr_sum -= nums[l]
                l += 1

        if ans == float('inf'):
            return 0

        return ans

