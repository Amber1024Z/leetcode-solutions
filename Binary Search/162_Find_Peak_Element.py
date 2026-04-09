class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: log(n)
        space: O(1)
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            # nums[mid] >= nums[mid + 1]
            else:
                # mid could be answer
                r = mid

        # when left == right, it's our ans, we can return either one
        return l
        