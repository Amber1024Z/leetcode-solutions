class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        seach from last index to the first index, we keep track of the leftmost index that can jump to the end, if we can 
        jump to that index from the first index, then we can jump to the end

        time: O(n), we traverse the array once
        space: O(1), we only need a variable to keep track of the leftmost index 
        """
        last_position = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last_position:
                last_position = i
        
        return last_position == 0