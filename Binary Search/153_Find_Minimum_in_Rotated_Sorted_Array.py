class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        # since it's ordered, findn first element smaller than previous segment
        while l < r:
            m = (l + r) // 2

            # serach on left, m could be answer
            if nums[m] < nums[r]:
                r = m 
            else: # nums[mid] >= nums[r], we should search min on right, skip m
                l = m + 1

        return nums[r]


        