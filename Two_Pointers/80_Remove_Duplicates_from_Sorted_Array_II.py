class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        time: O(n) where n is the length of nums, we traverse the array once
        space: O(1), we only use a constant amount of extra space for the two pointers
        """
            
        # slow pointer started from i = 2
        i = 2

        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i

        