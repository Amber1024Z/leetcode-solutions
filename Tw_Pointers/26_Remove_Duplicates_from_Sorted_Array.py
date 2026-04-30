class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        time complexity: O(n), where n is the length of nums, we traverse the array once
        space complexity: O(1), we only use a constant amount of extra space for the two pointers
        """
        # slow pointer, represents next position for non-duplicate element should be placed
        i = 1

        # since first element is always non-duplicate, we start from second element
        for j in range(1, len(nums)):
            # nums[i - 1] represents the last non-duplicate element
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        # since i will 1 step ahead of last non-duplicate element, it represents the length of non-duplicate elements
        return i