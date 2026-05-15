class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        time: O(n) because we traverse the nums array at most twice.
        space: O(1) because we are modifying the nums array in-place and not using any additional data structures.
        """

        # if nums is decreasing order, reverse whole nums
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            return nums.reverse()

        # i will stop at reverse idx because nums[i] < nums[i + 1]
        j = len(nums) - 1

        # scan from right to left to find first num > nums[i]
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]
         
        
        