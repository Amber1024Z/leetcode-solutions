class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n) we traverse the array once
        space: O(1) we only use constant space to store max_so_far, min_so_far and res
        """

        if len(nums) == 1:
            return nums[0]

        max_so_far = nums[0]
        # we have to track min num since this questions required product, future may encounter another negative number
        min_so_far = nums[0]
        res = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            """  3 options
            1. begining from itself 
            2. times max, if both are positive number, product will increase
            3. times min, if both are negative. product will also increase
            """
            temp_max = max(curr, curr * max_so_far, curr * min_so_far)
            temp_min = min(curr, curr * max_so_far, curr * min_so_far)

            max_so_far = temp_max
            min_so_far = temp_min

            res = max(max_so_far, res)
        return res

        