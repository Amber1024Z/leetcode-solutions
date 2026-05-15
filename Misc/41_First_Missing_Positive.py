class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time: O(n)
        space: O(1), in-place algorithm
        """
        # ans must fall into [1, n + 1],put num into correct pos
        i = 0

        while i < len(nums):
            # j represent correct pos for number, ex: nums[0] = 2, need to put 2 to idx 1 which is 2 - 1
            j = nums[i] - 1
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            # negative number, number > len(nums), or number is alreay in correct pos, can skip
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        # all numbers are in right pos, return len(nums) + 1
        return len(nums) + 1


