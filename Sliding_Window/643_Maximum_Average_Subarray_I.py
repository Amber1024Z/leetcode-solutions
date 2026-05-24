class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        
        time:O(n)
        space: O(1)
        """

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            # each time add new nums[i], we should remove left most num
            curr_sum = curr_sum + nums[i] - nums[i - k]
            max_sum  = max(max_sum, curr_sum)

        return float(max_sum) / k