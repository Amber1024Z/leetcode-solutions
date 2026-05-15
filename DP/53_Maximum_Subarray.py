class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        time: O(n) because we traverse the nums array once.
        space: O(1) 
        """
        current_sum = 0
        largest_sum = float('-inf')

        for n in nums:
            current_sum += n
            
            # update largest_sum first, because if all nums are negative
            if current_sum > largest_sum:
                largest_sum = current_sum
            
            if current_sum < 0:
                current_sum = 0 
        
        return largest_sum  