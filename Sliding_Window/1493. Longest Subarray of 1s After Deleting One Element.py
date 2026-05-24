class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1)
        """
        l = 0
        ans = 0
        zero = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zero += 1
            
            while zero > 1:
                # shrink from left
                if nums[l] == 0:
                    zero -= 1
            
                l += 1

            # since we will remove 0, thus it's r - l
            # also even array only contains 1, we still need to remove 1 num
            ans = max(ans, r - l)

        return ans




            