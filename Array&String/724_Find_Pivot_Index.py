class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        left_sum == total_sum - left_sum - nums[i] == right_sum
        time: O(n)
        space: O(1)
        """
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            # if not equal, add left nums[i] to left_sum
            left_sum += nums[i]

        return -1