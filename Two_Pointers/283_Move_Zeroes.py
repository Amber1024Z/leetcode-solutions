class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        time: O(n)
        space: O(1)
        """

        # i always point to first zero
        i = 0

        # j find non-zero element
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                # after swap, i += 1, point to 0
                i += 1

            